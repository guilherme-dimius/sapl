from _hashlib import new
from datetime import date
from operator import xor

from django.contrib.contenttypes.models import ContentType

from sapl.comissoes.models import Participacao, Comissao
from sapl.parlamentares.models import Legislatura, Parlamentar, Partido
from sapl.sessao.models import TipoResultadoVotacao
from sapl.utils import normalize


def adjust_tipoafastamento(new, old):
    assert xor(old.ind_afastamento, old.ind_fim_mandato)
    if old.ind_afastamento:
        new.indicador = 'A'
    elif old.ind_fim_mandato:
        new.indicador = 'F'

    if old.des_dispositivo is None:
        new.dispositivo = ''


def adjust_tipo_comissao(new, old):
    if old.des_dispositivo_regimental is None:
        new.dispositivo_regimental = ''


def adjust_statustramitacao(new, old):
    if old.ind_fim_tramitacao:
        new.indicador = 'F'
    elif old.ind_retorno_tramitacao:
        new.indicador = 'R'
    else:
        new.indicador = ''


def adjust_tipo_autor(new, old):
    model_apontado = normalize(new.descricao.lower()).replace(' ', '')
    content_types = ContentType.objects.filter(model=model_apontado)
    assert len(content_types) <= 1
    new.content_type = content_types[0] if content_types else None


def adjust_tiporesultadovotacao(new, old):
    if 'aprova' in new.nome.lower():
        new.natureza = TipoResultadoVotacao.NATUREZA_CHOICES.aprovado
    elif 'rejeita' in new.nome.lower():
        new.natureza = TipoResultadoVotacao.NATUREZA_CHOICES.rejeitado
    elif 'retirado' in new.nome.lower():
        new.natureza = TipoResultadoVotacao.NATUREZA_CHOICES.rejeitado
    else:
        new.natureza = ''


def adjust_orgao(new, old):
    if not new.endereco:
        new.endereco = ''
    if not new.telefone:
        new.telefone = ''


def adjust_assunto_norma(new, old):
    if not new.descricao:
        new.descricao = ''


def adjust_comissao(new, old):
    if not old.dat_extincao and not old.dat_fim_comissao:
        new.ativa = True
    elif (old.dat_extincao and date.today() < new.data_extincao or
          old.dat_fim_comissao and date.today() < new.data_fim_comissao):
        new.ativa = True
    else:
        new.ativa = False


def adjust_parlamentar(new, old):
    new.municipio_residencia = 'Jataí'
    new.uf_residencia = 'GO'

    if not new.nivel_instrucao_id:
        new.nivel_instrucao = None

    if not new.situacao_militar_id:
        new.situacao_militar = None


def adjust_mandato(new, old):
    if old.dat_fim_mandato:
        new.data_fim_mandato = old.dat_fim_mandato
    if not new.data_fim_mandato:
        legislatura = Legislatura.objects.latest('data_fim')
        new.data_fim_mandato = legislatura.data_fim
        new.data_expedicao_diploma = legislatura.data_inicio
    if not new.data_inicio_mandato:
        new.data_inicio_mandato = new.legislatura.data_inicio
        new.data_fim_mandato = new.legislatura.data_fim

    if new.tipo_afastamento_id == 0:
        new.tipo_afastamento_id = None


def adjust_composicao(new, old):
    new.save()
    Participacao.objects.filter(composicao=new).delete()
    p = Participacao()
    p.composicao = new
    p.parlamentar_id = getattr(old, 'cod_parlamentar')
    p.cargo_id = getattr(old, 'cod_cargo')
    p.titulo = getattr(old, 'ind_titular')
    p.data_designacao = getattr(old, 'dat_designacao')
    p.data_desligamento = getattr(old, 'dat_desligamento')
    p.motivo_desligamento = getattr(old, 'des_motivo_desligamento')
    p.observacao = getattr(old, 'obs_composicao')
    p.save()


def adjust_autor(new, old):

    if old.cod_parlamentar:
        new.nome = Parlamentar.objects.get(
            pk=old.cod_parlamentar).nome_parlamentar
        new.object_id = old.cod_parlamentar
        new.content_type = ContentType.objects.get_for_model(Parlamentar)

    if old.cod_comissao:
        new.nome = Comissao.objects.get(pk=old.cod_comissao).nome
        new.object_id = old.cod_comissao
        new.content_type = ContentType.objects.get_for_model(Comissao)

    if not new.cargo:
        new.cargo = ''


def adjust_sessaoplenaria(new, old):
    if old.ind_iniciada is None:
        new.iniciada = False
        new.finalizada = True
    elif old.ind_iniciada == 1:
        new.iniciada = True
        new.finalizada = False
    else:
        new.iniciada = False
        new.finalizada = False

    if new.url_audio is None:
        new.url_audio = ''
    if new.url_video is None:
        new.url_video = ''

    new.expedientesessao_set.all().delete()
