from datetime import date
from operator import xor

from django.contrib.contenttypes.models import ContentType

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
