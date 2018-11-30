from sapl.audiencia.models import AnexoAudienciaPublica, AudienciaPublica, TipoAudienciaPublica
from sapl.base.models import AppConfig, Autor, CasaLegislativa, TipoAutor
from sapl.comissoes.models import CargoComissao, Comissao, Composicao, Participacao, Periodo, Reuniao, TipoComissao
from sapl.comissoes.models import DocumentoAcessorio as ComissoesDocumentoAcessorio
from sapl.compilacao.models import Dispositivo, Nota, PerfilEstruturalTextoArticulado, Publicacao, TextoArticulado, TipoDispositivo, TipoDispositivoRelationship, TipoNota, TipoPublicacao, TipoTextoArticulado, TipoVide, VeiculoPublicacao, Vide
from sapl.lexml.models import LexmlProvedor, LexmlPublicador
from sapl.materia.models import AcompanhamentoMateria, Anexada, AssuntoMateria, Autoria, DespachoInicial, DocumentoAcessorio, MateriaAssunto, MateriaLegislativa, Numeracao, Orgao, Origem, Parecer, Proposicao, RegimeTramitacao, Relatoria, StatusTramitacao, TipoDocumento, TipoFimRelatoria, TipoMateriaLegislativa, TipoProposicao, Tramitacao, UnidadeTramitacao
from sapl.norma.models import AnexoNormaJuridica, AssuntoNorma, AutoriaNorma, LegislacaoCitada, NormaJuridica, NormaRelacionada, TipoNormaJuridica, TipoVinculoNormaJuridica
from sapl.painel.models import Cronometro, Painel
from sapl.parlamentares.models import CargoMesa, Coligacao, ComposicaoColigacao, ComposicaoMesa, Dependente, Filiacao, Frente, Legislatura, Mandato, NivelInstrucao, Parlamentar, Partido, SessaoLegislativa, SituacaoMilitar, TipoAfastamento, TipoDependente, Votante
from sapl.protocoloadm.models import AcompanhamentoDocumento, DocumentoAcessorioAdministrativo, DocumentoAdministrativo, Protocolo, StatusTramitacaoAdministrativo, TipoDocumentoAdministrativo, TramitacaoAdministrativo
from sapl.s3.adjust import adjust_tipoafastamento, adjust_tipo_comissao,\
    adjust_statustramitacao, adjust_tipo_autor, adjust_tiporesultadovotacao,\
    adjust_orgao, adjust_assunto_norma, adjust_comissao, adjust_parlamentar
from sapl.s3.models import (
    _AcompMateria, _Afastamento, _Anexada, _AssuntoNorma, _Autor, _Autoria,
    _CargoComissao, _CargoMesa, _Comissao, _ComposicaoComissao, _ComposicaoMesa,
    _CronometroAparte, _CronometroDiscurso, _CronometroOrdem, _DespachoInicial,
    _Dispositivo, _DocumentoAcessorio, _DocumentoAcessorioAdministrativo,
    _DocumentoAdministrativo, _ExpedienteMateria, _ExpedienteSessaoPlenaria,
    _Filiacao, _LegislacaoCitada, _Legislatura, _Localidade, _Mandato,
    _MateriaLegislativa, _MesaSessaoPlenaria, _NormaJuridica, _Numeracao,
    _OradoresExpediente, _OrdemDia, _OrdemDiaPresenca, _Orgao, _Origem,
    _Parlamentar, _Partido, _PeriodoCompComissao, _PeriodoCompMesa, _Proposicao,
    _Protocolo, _RegimeTramitacao, _RegistroPresencaOrdem,
    _RegistroPresencaSessao, _RegistroVotacao, _RegistroVotacaoParlamentar,
    _Relatoria, _ReuniaoComissao, _SessaoLegislativa, _SessaoPlenaria,
    _SessaoPlenariaPresenca, _StatusTramitacao, _StatusTramitacaoAdministrativo,
    _StatusTramitacaoParecer, _TipoAfastamento, _TipoAutor, _TipoComissao,
    _TipoDependente, _TipoDocumento, _TipoDocumentoAdministrativo,
    _TipoExpediente, _TipoFimRelatoria, _TipoMateriaLegislativa,
    _TipoNormaJuridica, _TipoParecer, _TipoProposicao, _TipoResultadoVotacao,
    _TipoSessaoPlenaria, _TipoSituacaoMateria, _TipoSituacaoMilitar,
    _TipoSituacaoNorma, _Tramitacao, _TramitacaoAdministrativo,
    _TramitacaoParecer, _UnidadeTramitacao, _VinculoNormaJuridica)
from sapl.sessao.models import Bancada, Bloco, CargoBancada, ExpedienteMateria, ExpedienteSessao, IntegranteMesa, OcorrenciaSessao, Orador, OradorExpediente, OrdemDia, PresencaOrdemDia, RegistroVotacao, ResumoOrdenacao, SessaoPlenaria, SessaoPlenariaPresenca, TipoExpediente, TipoResultadoVotacao, TipoSessaoPlenaria, VotoParlamentar


mapa = [
    {
        'name': 'nao importar',
        's31_model': [
            AudienciaPublica,
            TipoAudienciaPublica,
            CasaLegislativa,
            AppConfig,
            NivelInstrucao,
            Frente,
            AssuntoMateria,
            TipoVinculoNormaJuridica,
            CargoBancada,
            Bloco,
            ResumoOrdenacao,
            LexmlProvedor,
            LexmlPublicador,
            Painel,
            Cronometro,
            TipoNota,
            TipoVide,
            TipoDispositivo,
            TipoPublicacao,
            VeiculoPublicacao,
            Vide,
            Nota,
            Dispositivo,
            Publicacao,
            TipoDispositivoRelationship,
            TextoArticulado,
            TipoTextoArticulado,
            PerfilEstruturalTextoArticulado,
            AcompanhamentoDocumento,
            Bancada,
            Coligacao,
            AnexoAudienciaPublica,
            AcompanhamentoMateria,
            ComposicaoColigacao,
            AnexoNormaJuridica,
            OcorrenciaSessao,
            ComissoesDocumentoAcessorio,
            TipoProposicao,
            Dependente,
            'TipoProposicao_perfis',
            'Frente_parlamentares',
            'Bloco_partidos',

        ]
    },
    {
        'name': '_legislatura',
        's30_model': _Legislatura,
        's31_model': Legislatura,
        'fields': {
            'id': 'num_legislatura',
            'numero': 'num_legislatura',
            'data_inicio': 'dat_inicio',
            'data_fim': 'dat_fim',
            'data_eleicao': 'dat_eleicao',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_partido',
        's30_model': _Partido,
        's31_model': Partido,
        'fields': {
            'id': 'cod_partido',
            'sigla': 'sgl_partido',
            'nome': 'nom_partido',
            'data_criacao': 'dat_criacao',
            'data_extincao': 'dat_extincao',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipodependente',
        's30_model': _TipoDependente,
        's31_model': TipoDependente,
        'fields': {
            'id': 'tip_dependente',
            'descricao': 'des_tipo_dependente',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipoafastamento',
        's30_model': _TipoAfastamento,
        's31_model': TipoAfastamento,
        'fields': {
            'id': 'tip_afastamento',
            'descricao': 'des_afastamento',
            'dispositivo': 'des_dispositivo',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_tipoafastamento,
    },
    {
        'name': '_cargomesa',
        's30_model': _CargoMesa,
        's31_model': CargoMesa,
        'fields': {
            'id': 'cod_cargo',
            'descricao': 'des_cargo',
            'unico': 'ind_unico',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipocomissao',
        's30_model': _TipoComissao,
        's31_model': TipoComissao,
        'fields': {
            'id': 'tip_comissao',
            'nome': 'nom_tipo_comissao',
            'natureza': 'sgl_natureza_comissao',
            'sigla': 'sgl_tipo_comissao',
            'dispositivo_regimental': 'des_dispositivo_regimental',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_tipo_comissao
    },

    {
        'name': '_periodocompcomissao',
        's30_model': _PeriodoCompComissao,
        's31_model': Periodo,
        'fields': {
            'id': 'cod_periodo_comp',
            'data_inicio': 'dat_inicio_periodo',
            'data_fim': 'dat_fim_periodo',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_cargocomissao',
        's30_model': _CargoComissao,
        's31_model': CargoComissao,
        'fields': {
            'id': 'cod_cargo',
            'nome': 'des_cargo',
            'unico': 'ind_unico',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipomaterialegislativa',
        's30_model': _TipoMateriaLegislativa,
        's31_model': TipoMateriaLegislativa,
        'fields': {
            'id': 'tip_materia',
            'sigla': 'sgl_tipo_materia',
            'descricao': 'des_tipo_materia',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_statustramitacao',
        's30_model': _StatusTramitacao,
        's31_model': StatusTramitacao,
        'fields': {
            'id': 'cod_status',
            'sigla': 'sgl_status',
            'descricao': 'des_status',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_statustramitacao
    },
    {
        'name': '_statustramitacaoadministrativo',
        's30_model': _StatusTramitacaoAdministrativo,
        's31_model': StatusTramitacaoAdministrativo,
        'fields': {
            'id': 'cod_status',
            'sigla': 'sgl_status',
            'descricao': 'des_status',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_statustramitacao
    },

    {
        'name': '_tipoautor',
        's30_model': _TipoAutor,
        's31_model': TipoAutor,
        'fields': {
            'id': 'tip_autor',
            'descricao': 'des_tipo_autor',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_tipo_autor
    },
    {
        'name': '_tipodocumento',
        's30_model': _TipoDocumento,
        's31_model': TipoDocumento,
        'fields': {
            'id': 'tip_documento',
            'descricao': 'des_tipo_documento',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipodocumentoadministrativo',
        's30_model': _TipoDocumentoAdministrativo,
        's31_model': TipoDocumentoAdministrativo,
        'fields': {
            'id': 'tip_documento',
            'sigla': 'sgl_tipo_documento',
            'descricao': 'des_tipo_documento',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipoexpediente',
        's30_model': _TipoExpediente,
        's31_model': TipoExpediente,
        'fields': {
            'id': 'cod_expediente',
            'descricao': 'nom_expediente',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipofimrelatoria',
        's30_model': _TipoFimRelatoria,
        's31_model': TipoFimRelatoria,
        'fields': {
            'id': 'tip_fim_relatoria',
            'descricao': 'des_fim_relatoria',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiponormajuridica',
        's30_model': _TipoNormaJuridica,
        's31_model': TipoNormaJuridica,
        'fields': {
            'id': 'tip_norma',
            'sigla': 'sgl_tipo_norma',
            'descricao': 'des_tipo_norma',
            'equivalente_lexml': 'voc_lexml',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiporesultadovotacao',
        's30_model': _TipoResultadoVotacao,
        's31_model': TipoResultadoVotacao,
        'fields': {
            'id': 'tip_resultado_votacao',
            'nome': 'nom_resultado',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_tiporesultadovotacao
    },
    {
        'name': '_tiposessaoplenaria',
        's30_model': _TipoSessaoPlenaria,
        's31_model': TipoSessaoPlenaria,
        'fields': {
            'id': 'tip_sessao',
            'nome': 'nom_sessao',
            'quorum_minimo': 'num_minimo',
            'ind_excluido': 'ind_excluido',
        }
    },
    {
        'name': '_assuntonorma',
        's30_model': _AssuntoNorma,
        's31_model': AssuntoNorma,
        'fields': {
            'id': 'cod_assunto',
            'assunto': 'des_assunto',
            'descricao': 'des_estendida',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_assunto_norma
    },
    {
        'name': '_orgao',
        's30_model': _Orgao,
        's31_model': Orgao,
        'fields': {
            'id': 'cod_orgao',
            'nome': 'nom_orgao',
            'sigla': 'sgl_orgao',
            'unidade_deliberativa': 'ind_unid_deliberativa',
            'endereco': 'end_orgao',
            'telefone': 'num_tel_orgao',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_orgao
    },
    {
        'name': '_origem',
        's30_model': _Origem,
        's31_model': Origem,
        'fields': {
            'id': 'cod_origem',
            'sigla': 'sgl_origem',
            'nome': 'nom_origem',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_regimetramitacao',
        's30_model': _RegimeTramitacao,
        's31_model': RegimeTramitacao,
        'fields': {
            'id': 'cod_regime_tramitacao',
            'descricao': 'des_regime_tramitacao',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiposituacaomilitar',
        's30_model': _TipoSituacaoMilitar,
        's31_model': SituacaoMilitar,
        'fields': {
            'id': 'tip_situacao_militar',
            'descricao': 'des_tipo_situacao',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_comissao',
        's30_model': _Comissao,
        's31_model': Comissao,
        'fields': {
            'id': 'cod_comissao',
            'tipo_id': 'tip_comissao',
            'nome': 'nom_comissao',
            'sigla': 'sgl_comissao',
            'data_criacao': 'dat_criacao',
            'data_extincao': 'dat_extincao',
            'apelido_temp': 'nom_apelido_temp',
            'data_instalacao_temp': 'dat_instalacao_temp',
            'data_final_prevista_temp': 'dat_final_prevista_temp',
            'data_prorrogada_temp': 'dat_prorrogada_temp',
            'data_fim_comissao': 'dat_fim_comissao',
            'secretario': 'nom_secretario',
            'telefone_reuniao': 'num_tel_reuniao',
            'endereco_secretaria': 'end_secretaria',
            'telefone_secretaria': 'num_tel_secretaria',
            'fax_secretaria': 'num_fax_secretaria',
            'agenda_reuniao': 'des_agenda_reuniao',
            'local_reuniao': 'loc_reuniao',
            'finalidade': 'txt_finalidade',
            'email': 'end_email',
            'unidade_deliberativa': 'ind_unid_deliberativa',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_comissao
    },
    {
        'name': '_sessaolegislativa',
        's30_model': _SessaoLegislativa,
        's31_model': SessaoLegislativa,
        'fields': {
            'id': 'cod_sessao_leg',
            'legislatura_id': 'num_legislatura',
            'numero': 'num_sessao_leg',
            'tipo': 'tip_sessao_leg',
            'data_inicio': 'dat_inicio',
            'data_fim': 'dat_fim',
            'data_inicio_intervalo': 'dat_inicio_intervalo',
            'data_fim_intervalo': 'dat_fim_intervalo',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_parlamentar',
        's30_model': _Parlamentar,
        's31_model': Parlamentar,
        'fields': {
            'id': 'cod_parlamentar',
            'nivel_instrucao_id': 'cod_nivel_instrucao',
            'situacao_militar_id': 'tip_situacao_militar',
            'nome_completo': 'nom_completo',
            'nome_parlamentar': 'nom_parlamentar',
            'sexo': 'sex_parlamentar',
            'data_nascimento': 'dat_nascimento',
            'cpf': 'num_cpf',
            'rg': 'num_rg',
            'titulo_eleitor': 'num_tit_eleitor',
            'numero_gab_parlamentar': 'num_gab_parlamentar',
            'telefone': 'num_tel_parlamentar',
            'fax': 'num_fax_parlamentar',
            'endereco_residencia': 'end_residencial',
            'cep_residencia': 'num_cep_resid',
            'telefone_residencia': 'num_tel_resid',
            'fax_residencia': 'num_fax_resid',
            'endereco_web': 'end_web',
            'profissao': 'nom_profissao',
            'email': 'end_email',
            'locais_atuacao': 'des_local_atuacao',
            'ativo': 'ind_ativo',
            'biografia': 'txt_biografia',
            'ind_excluido': 'ind_excluido'
        },
        'adjust': adjust_parlamentar
    },
]

mapa_a_processar = [
    # TODO: processar






    {
        'name': '_afastamento',
        's30_model': _Afastamento,
        's31_model': None,
        'fields': {
            '': 'cod_afastamento',
            '': 'cod_parlamentar',
            '': 'cod_mandato',
            '': 'num_legislatura',
            '': 'tip_afastamento',
            '': 'dat_inicio_afastamento',
            '': 'dat_fim_afastamento',
            '': 'cod_parlamentar_suplente',
            '': 'txt_observacao',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_anexada',
        's30_model': _Anexada,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_materia_principal',
                '': 'cod_materia_anexada',
                '': 'dat_anexacao',
                '': 'dat_desanexacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_autor',
        's30_model': _Autor,
        's31_model': None,
        'fields': {
            '': 'cod_autor',
            '': 'cod_partido',
                '': 'cod_comissao',
                '': 'cod_bancada',
                '': 'cod_parlamentar',
                '': 'tip_autor',
                '': 'nom_autor',
                '': 'des_cargo',
                '': 'col_username',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_autoria',
        's30_model': _Autoria,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_autor',
                '': 'cod_materia',
                '': 'ind_primeiro_autor',
                'ind_excluido': 'ind_excluido'
        }
    },

    {
        'name': '_composicaocomissao',
        's30_model': _ComposicaoComissao,
        's31_model': None,
        'fields': {
            '': 'cod_comp_comissao',
            '': 'cod_parlamentar',
                '': 'cod_comissao',
                '': 'cod_periodo_comp',
                '': 'cod_cargo',
                '': 'ind_titular',
                '': 'dat_designacao',
                '': 'dat_desligamento',
                '': 'des_motivo_desligamento',
                '': 'obs_composicao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_composicaomesa',
        's30_model': _ComposicaoMesa,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_parlamentar',
                '': 'cod_sessao_leg',
                '': 'cod_periodo_comp',
                '': 'cod_cargo',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_cronometroaparte',
        's30_model': _CronometroAparte,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'int_reset',
                '': 'int_start',
                '': 'int_stop'
        }
    },
    {
        'name': '_cronometrodiscurso',
        's30_model': _CronometroDiscurso,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'int_reset',
                '': 'int_start',
                '': 'int_stop'
        }
    },
    {
        'name': '_cronometroordem',
        's30_model': _CronometroOrdem,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'int_reset',
                '': 'int_start',
                '': 'int_stop'
        }
    },
    {
        'name': '_despachoinicial',
        's30_model': _DespachoInicial,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_materia',
                '': 'num_ordem',
                '': 'cod_comissao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_dispositivo',
        's30_model': _Dispositivo,
        's31_model': None,
        'fields': {
            '': 'cod_dispositivo',
            '': 'num_ordem',
                '': 'num_ordem_bloco_atualizador',
                '': 'num_nivel',
                '': 'num_dispositivo_0',
                '': 'num_dispositivo_1',
                '': 'num_dispositivo_2',
                '': 'num_dispositivo_3',
                '': 'num_dispositivo_4',
                '': 'num_dispositivo_5',
                '': 'txt_rotulo',
                '': 'txt_texto',
                '': 'txt_texto_atualizador',
                '': 'dat_inicio_vigencia',
                '': 'dat_fim_vigencia',
                '': 'dat_inicio_eficacia',
                '': 'dat_fim_eficacia',
                '': 'ind_visibilidade',
                '': 'ind_validade',
                '': 'tim_atualizacao_banco',
                '': 'cod_norma',
                '': 'cod_norma_publicada',
                '': 'cod_dispositivo_pai',
                '': 'cod_dispositivo_vigencia',
                '': 'cod_dispositivo_atualizador',
                '': 'cod_tipo_dispositivo',
                '': 'cod_publicacao'
        }
    },
    {
        'name': '_documentoacessorio',
        's30_model': _DocumentoAcessorio,
        's31_model': None,
        'fields': {
            '': 'cod_documento',
            '': 'cod_materia',
                '': 'tip_documento',
                '': 'nom_documento',
                '': 'dat_documento',
                '': 'nom_autor_documento',
                '': 'txt_ementa',
                '': 'txt_observacao',
                '': 'txt_indexacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_documentoacessorioadministrativo',
        's30_model': _DocumentoAcessorioAdministrativo,
        's31_model': None,
        'fields': {
            '': 'cod_documento_acessorio',
            '': 'cod_documento',
                '': 'tip_documento',
                '': 'nom_documento',
                '': 'nom_arquivo',
                '': 'dat_documento',
                '': 'nom_autor_documento',
                '': 'txt_assunto',
                '': 'txt_indexacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_documentoadministrativo',
        's30_model': _DocumentoAdministrativo,
        's31_model': None,
        'fields': {
            '': 'cod_documento',
            '': 'tip_documento',
                '': 'num_documento',
                '': 'ano_documento',
                '': 'dat_documento',
                '': 'num_protocolo',
                '': 'txt_interessado',
                '': 'cod_autor',
                '': 'num_dias_prazo',
                '': 'dat_fim_prazo',
                '': 'ind_tramitacao',
                '': 'txt_assunto',
                '': 'txt_observacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_expedientemateria',
        's30_model': _ExpedienteMateria,
        's31_model': None,
        'fields': {
            '': 'cod_ordem',
            '': 'cod_sessao_plen',
                '': 'cod_materia',
                '': 'dat_ordem',
                '': 'txt_observacao',
                '': 'txt_tramitacao',
                'ind_excluido': 'ind_excluido',
                '': 'num_ordem',
                '': 'txt_resultado',
                '': 'tip_votacao',
                '': 'ind_votacao_iniciada',
                '': 'dat_ultima_votacao'
        }
    },
    {
        'name': '_expedientesessaoplenaria',
        's30_model': _ExpedienteSessaoPlenaria,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_sessao_plen',
                '': 'cod_expediente',
                '': 'txt_expediente',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_filiacao',
        's30_model': _Filiacao,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'dat_filiacao',
                '': 'cod_parlamentar',
                '': 'cod_partido',
                '': 'dat_desfiliacao',
                'ind_excluido': 'ind_excluido',
                '': 'teste'
        }
    },
    {
        'name': '_legislacaocitada',
        's30_model': _LegislacaoCitada,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_materia',
                '': 'cod_norma',
                '': 'des_disposicoes',
                '': 'des_parte',
                '': 'des_livro',
                '': 'des_titulo',
                '': 'des_capitulo',
                '': 'des_secao',
                '': 'des_subsecao',
                '': 'des_artigo',
                '': 'des_paragrafo',
                '': 'des_inciso',
                '': 'des_alinea',
                '': 'des_item',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_localidade',
        's30_model': _Localidade,
        's31_model': None,
        'fields': {
            '': 'cod_localidade',
            '': 'nom_localidade',
                '': 'nom_localidade_pesq',
                '': 'tip_localidade',
                '': 'sgl_uf',
                '': 'sgl_regiao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_mandato',
        's30_model': _Mandato,
        's31_model': None,
        'fields': {
            '': 'cod_mandato',
            '': 'cod_parlamentar',
            '': 'tip_afastamento',
            '': 'num_legislatura',
            '': 'cod_coligacao',
            '': 'dat_inicio_mandato',
            '': 'tip_causa_fim_mandato',
            '': 'dat_fim_mandato',
            '': 'num_votos_recebidos',
            '': 'dat_expedicao_diploma',
            '': 'txt_observacao',
            '': 'ind_titular',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_materialegislativa',
        's30_model': _MateriaLegislativa,
        's31_model': None,
        'fields': {
            '': 'cod_materia',
            '': 'tip_id_basica',
                '': 'num_protocolo',
                '': 'num_protocolo_spdo',
                '': 'num_ident_basica',
                '': 'ano_ident_basica',
                '': 'dat_apresentacao',
                '': 'tip_apresentacao',
                '': 'cod_regime_tramitacao',
                '': 'dat_publicacao',
                '': 'tip_origem_externa',
                '': 'num_origem_externa',
                '': 'ano_origem_externa',
                '': 'dat_origem_externa',
                '': 'cod_local_origem_externa',
                '': 'nom_apelido',
                '': 'num_dias_prazo',
                '': 'dat_fim_prazo',
                '': 'ind_tramitacao',
                '': 'ind_polemica',
                '': 'des_objeto',
                '': 'ind_complementar',
                '': 'txt_ementa',
                '': 'txt_indexacao',
                '': 'txt_observacao',
                '': 'cod_situacao',
                'ind_excluido': 'ind_excluido',
                '': 'txt_resultado',
                '': 'txt_cep',
                '': 'txt_latitude',
                '': 'txt_longitude',
                '': 'ind_publico'
        }
    },
    {
        'name': '_mesasessaoplenaria',
        's30_model': _MesaSessaoPlenaria,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_cargo',
                '': 'cod_sessao_leg',
                '': 'cod_parlamentar',
                '': 'cod_sessao_plen',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_normajuridica',
        's30_model': _NormaJuridica,
        's31_model': None,
        'fields': {
            '': 'cod_norma',
            '': 'tip_norma',
                '': 'cod_materia',
                '': 'num_norma',
                '': 'ano_norma',
                '': 'tip_esfera_federacao',
                '': 'dat_norma',
                '': 'dat_publicacao',
                '': 'des_veiculo_publicacao',
                '': 'num_pag_inicio_publ',
                '': 'num_pag_fim_publ',
                '': 'txt_ementa',
                '': 'txt_indexacao',
                '': 'txt_observacao',
                '': 'ind_complemento',
                '': 'cod_assunto',
                '': 'cod_situacao',
                'ind_excluido': 'ind_excluido',
                '': 'dat_vigencia',
                '': 'timestamp'
        }
    },
    {
        'name': '_numeracao',
        's30_model': _Numeracao,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_materia',
                '': 'num_ordem',
                '': 'tip_materia',
                '': 'num_materia',
                '': 'ano_materia',
                '': 'dat_materia',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_oradoresexpediente',
        's30_model': _OradoresExpediente,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_sessao_plen',
                '': 'cod_parlamentar',
                '': 'num_ordem',
                '': 'url_discurso',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_ordemdia',
        's30_model': _OrdemDia,
        's31_model': None,
        'fields': {
            '': 'cod_ordem',
            '': 'cod_sessao_plen',
                '': 'cod_materia',
                '': 'dat_ordem',
                '': 'txt_observacao',
                '': 'txt_tramitacao',
                'ind_excluido': 'ind_excluido',
                '': 'num_ordem',
                '': 'txt_resultado',
                '': 'tip_votacao',
                '': 'ind_votacao_iniciada',
                '': 'dat_ultima_votacao',
                '': 'tip_quorum'
        }
    },
    {
        'name': '_ordemdiapresenca',
        's30_model': _OrdemDiaPresenca,
        's31_model': None,
        'fields': {
            '': 'cod_parlamentar',
            'ind_excluido': 'ind_excluido',
                '': 'dat_ordem',
                '': 'dat_presenca',
                '': 'cod_ip',
                '': 'cod_mac',
                '': 'cod_perfil',
                '': 'ind_recontagem',
                '': 'num_id_quorum',
                '': 'cod_sessao_plen',
                '': 'cod_presenca_ordem_dia'
        }
    },

    {
        'name': '_periodocompmesa',
        's30_model': _PeriodoCompMesa,
        's31_model': None,
        'fields': {
            '': 'cod_periodo_comp',
            '': 'num_legislatura',
                '': 'dat_inicio_periodo',
                '': 'dat_fim_periodo',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_proposicao',
        's30_model': _Proposicao,
        's31_model': None,
        'fields': {
            '': 'cod_proposicao',
            '': 'cod_materia',
                '': 'cod_autor',
                '': 'tip_proposicao',
                '': 'dat_envio',
                '': 'dat_recebimento',
                '': 'txt_descricao',
                '': 'cod_mat_ou_doc',
                '': 'dat_devolucao',
                '': 'txt_justif_devolucao',
                '': 'txt_observacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_protocolo',
        's30_model': _Protocolo,
        's31_model': None,
        'fields': {
            '': 'cod_protocolo',
            '': 'num_protocolo',
                '': 'ano_protocolo',
                '': 'dat_protocolo',
                '': 'hor_protocolo',
                '': 'dat_timestamp',
                '': 'tip_protocolo',
                '': 'tip_processo',
                '': 'txt_interessado',
                '': 'cod_autor',
                '': 'txt_assunto_ementa',
                '': 'tip_documento',
                '': 'tip_materia',
                '': 'cod_documento',
                '': 'cod_materia',
                '': 'num_paginas',
                '': 'txt_observacao',
                '': 'ind_anulado',
                '': 'txt_user_anulacao',
                '': 'txt_ip_anulacao',
                '': 'txt_just_anulacao',
                '': 'timestamp_anulacao',
                '': 'num_protocolo_spdo'
        }
    },
    {
        'name': '_regimetramitacao',
        's30_model': _RegimeTramitacao,
        's31_model': None,
        'fields': {
            '': 'cod_regime_tramitacao',
            '': 'des_regime_tramitacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_registropresencaordem',
        's30_model': _RegistroPresencaOrdem,
        's31_model': None,
        'fields': {
            '': 'cod_registro_pre',
            '': 'cod_sessao_plen',
                '': 'num_id_quorum',
                '': 'ind_status_pre',
                '': 'dat_abre_pre',
                '': 'dat_fecha_pre',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_registropresencasessao',
        's30_model': _RegistroPresencaSessao,
        's31_model': None,
        'fields': {
            '': 'cod_registro_pre',
            '': 'cod_sessao_plen',
                '': 'num_id_quorum',
                '': 'ind_status_pre',
                '': 'dat_abre_pre',
                '': 'dat_fecha_pre',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_registrovotacao',
        's30_model': _RegistroVotacao,
        's31_model': None,
        'fields': {
            '': 'cod_votacao',
            '': 'tip_resultado_votacao',
                '': 'cod_materia',
                '': 'cod_ordem',
                '': 'num_votos_sim',
                '': 'num_votos_nao',
                '': 'num_abstencao',
                '': 'txt_observacao',
                'ind_excluido': 'ind_excluido',
                '': 'num_nao_votou'
        }
    },
    {
        'name': '_registrovotacaoparlamentar',
        's30_model': _RegistroVotacaoParlamentar,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_votacao',
                '': 'cod_parlamentar',
                'ind_excluido': 'ind_excluido',
                '': 'vot_parlamentar',
                '': 'txt_login'
        }
    },
    {
        'name': '_relatoria',
        's30_model': _Relatoria,
        's31_model': None,
        'fields': {
            '': 'cod_relatoria',
            '': 'cod_materia',
                '': 'cod_parlamentar',
                '': 'tip_fim_relatoria',
                '': 'cod_comissao',
                '': 'dat_desig_relator',
                '': 'dat_destit_relator',
                '': 'tip_apresentacao',
                '': 'txt_parecer',
                '': 'tip_conclusao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_reuniaocomissao',
        's30_model': _ReuniaoComissao,
        's31_model': None,
        'fields': {
            '': 'cod_reuniao',
            '': 'cod_comissao',
            '': 'num_reuniao',
            '': 'dat_inicio_reuniao',
            '': 'hr_inicio_reuniao',
            '': 'txt_observacao',
            'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_sessaoplenaria',
        's30_model': _SessaoPlenaria,
        's31_model': None,
        'fields': {
            '': 'cod_sessao_plen',
            '': 'cod_andamento_sessao',
                '': 'tip_sessao',
                '': 'cod_sessao_leg',
                '': 'num_legislatura',
                '': 'tip_expediente',
                '': 'dat_inicio_sessao',
                '': 'dia_sessao',
                '': 'hr_inicio_sessao',
                '': 'hr_fim_sessao',
                '': 'num_sessao_plen',
                '': 'dat_fim_sessao',
                '': 'url_audio',
                '': 'url_video',
                '': 'ind_iniciada',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_sessaoplenariapresenca',
        's30_model': _SessaoPlenariaPresenca,
        's31_model': None,
        'fields': {
            '': 'id',
            '': 'cod_sessao_plen',
                '': 'cod_parlamentar',
                'ind_excluido': 'ind_excluido',
                '': 'dat_presenca',
                '': 'cod_ip',
                '': 'cod_mac',
                '': 'cod_perfil',
                '': 'ind_recontagem'
        }
    },
    {
        'name': '_tramitacao',
        's30_model': _Tramitacao,
        's31_model': None,
        'fields': {
            '': 'cod_tramitacao',
            '': 'cod_status',
                '': 'cod_materia',
                '': 'dat_tramitacao',
                '': 'cod_unid_tram_local',
                '': 'dat_encaminha',
                '': 'cod_unid_tram_dest',
                '': 'ind_ult_tramitacao',
                '': 'ind_urgencia',
                '': 'sgl_turno',
                '': 'txt_tramitacao',
                '': 'dat_fim_prazo',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tramitacaoadministrativo',
        's30_model': _TramitacaoAdministrativo,
        's31_model': None,
        'fields': {
            '': 'cod_tramitacao',
            '': 'cod_documento',
                '': 'dat_tramitacao',
                '': 'cod_unid_tram_local',
                '': 'dat_encaminha',
                '': 'cod_unid_tram_dest',
                '': 'cod_status',
                '': 'ind_ult_tramitacao',
                '': 'txt_tramitacao',
                '': 'dat_fim_prazo',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tramitacaoparecer',
        's30_model': _TramitacaoParecer,
        's31_model': None,
        'fields': {
            '': 'cod_tramitacao',
            '': 'cod_documento',
                '': 'dat_tramitacao',
                '': 'cod_unid_tram_local',
                '': 'dat_encaminha',
                '': 'cod_unid_tram_dest',
                '': 'cod_status',
                '': 'ind_ult_tramitacao',
                '': 'txt_tramitacao',
                '': 'dat_fim_prazo',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_unidadetramitacao',
        's30_model': _UnidadeTramitacao,
        's31_model': None,
        'fields': {
            '': 'cod_unid_tramitacao',
            '': 'cod_comissao',
                '': 'cod_orgao',
                '': 'cod_parlamentar',
                '': 'cod_unid_spdo',
                '': 'txt_unid_spdo',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_vinculonormajuridica',
        's30_model': _VinculoNormaJuridica,
        's31_model': None,
        'fields': {
            '': 'cod_vinculo',
            '': 'cod_norma_referente',
                '': 'cod_norma_referida',
                '': 'tip_vinculo',
                'ind_excluido': 'ind_excluido'
        }
    }
]
