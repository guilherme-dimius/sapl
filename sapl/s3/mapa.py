from sapl.comissoes.models import TipoComissao, Periodo, CargoComissao
from sapl.legacy.migracao_dados import adjust_tipoafastamento
from sapl.materia.models import TipoMateriaLegislativa
from sapl.parlamentares.models import Legislatura, Partido, SessaoLegislativa,\
    TipoDependente, TipoAfastamento, CargoMesa
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


mapa = [
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
        'reset': True,
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
        }
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
            '': 'ord_tipo_materia',
            '': 'tip_materia',
            '': 'sgl_tipo_materia',
            '': 'des_tipo_materia',
            'ind_excluido': 'ind_excluido'
        }
    },






    {
        'name': '_statustramitacao',
        's30_model': _StatusTramitacao,
        's31_model': None,
        'fields': {
            '': 'cod_status',
            '': 'sgl_status',
                '': 'des_status',
                '': 'ind_fim_tramitacao',
                '': 'ind_retorno_tramitacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_statustramitacaoadministrativo',
        's30_model': _StatusTramitacaoAdministrativo,
        's31_model': None,
        'fields': {
            '': 'cod_status',
            '': 'sgl_status',
                '': 'des_status',
                '': 'ind_fim_tramitacao',
                '': 'ind_retorno_tramitacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_statustramitacaoparecer',
        's30_model': _StatusTramitacaoParecer,
        's31_model': None,
        'fields': {
            '': 'cod_status',
            '': 'sgl_status',
                '': 'des_status',
                '': 'ind_fim_tramitacao',
                '': 'ind_retorno_tramitacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipoautor',
        's30_model': _TipoAutor,
        's31_model': None,
        'fields': {
            '': 'tip_autor',
            '': 'des_tipo_autor',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipodocumento',
        's30_model': _TipoDocumento,
        's31_model': None,
        'fields': {
            '': 'tip_documento',
            '': 'des_tipo_documento',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipodocumentoadministrativo',
        's30_model': _TipoDocumentoAdministrativo,
        's31_model': None,
        'fields': {
            '': 'tip_documento',
            '': 'sgl_tipo_documento',
                '': 'des_tipo_documento',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipoexpediente',
        's30_model': _TipoExpediente,
        's31_model': None,
        'fields': {
            '': 'cod_expediente',
            '': 'nom_expediente',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipofimrelatoria',
        's30_model': _TipoFimRelatoria,
        's31_model': None,
        'fields': {
            '': 'tip_fim_relatoria',
            '': 'des_fim_relatoria',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiponormajuridica',
        's30_model': _TipoNormaJuridica,
        's31_model': None,
        'fields': {
            '': 'tip_norma',
            '': 'sgl_tipo_norma',
                '': 'des_tipo_norma',
                '': 'voc_lexml',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tipoproposicao',
        's30_model': _TipoProposicao,
        's31_model': None,
        'fields': {
            '': 'tip_proposicao',
            '': 'des_tipo_proposicao',
                '': 'ind_mat_ou_doc',
                '': 'tip_mat_ou_doc',
                '': 'nom_modelo',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiporesultadovotacao',
        's30_model': _TipoResultadoVotacao,
        's31_model': None,
        'fields': {
            '': 'tip_resultado_votacao',
            '': 'nom_resultado',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiposessaoplenaria',
        's30_model': _TipoSessaoPlenaria,
        's31_model': None,
        'fields': {
            '': 'tip_sessao',
            '': 'nom_sessao',
                'ind_excluido': 'ind_excluido',
                '': 'num_minimo'
        }
    },
    {
        'name': '_tiposituacaomateria',
        's30_model': _TipoSituacaoMateria,
        's31_model': None,
        'fields': {
            '': 'tip_situacao_materia',
            '': 'des_tipo_situacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiposituacaomilitar',
        's30_model': _TipoSituacaoMilitar,
        's31_model': None,
        'fields': {
            '': 'tip_situacao_militar',
            '': 'des_tipo_situacao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_tiposituacaonorma',
        's30_model': _TipoSituacaoNorma,
        's31_model': None,
        'fields': {
            '': 'tip_situacao_norma',
            '': 'des_tipo_situacao',
                'ind_excluido': 'ind_excluido'
        }
    },











    {
        'name': '_sessaolegislativa',
        's30_model': _SessaoLegislativa,
        's31_model': SessaoLegislativa,
        'fields': {
            '': 'cod_sessao_leg',
            '': 'num_legislatura',
            '': 'num_sessao_leg',
            '': 'tip_sessao_leg',
            '': 'dat_inicio',
            '': 'dat_fim',
            '': 'dat_inicio_intervalo',
            '': 'dat_fim_intervalo',
            'ind_excluido': 'ind_excluido'
        }
    },


    {
        'name': '_acompmateria',
        's30_model': _AcompMateria,
        's31_model': None,
        'fields': {
            '': 'cod_cadastro',
            '': 'cod_materia',
            '': 'end_email',
            '': 'txt_hash',
            'ind_excluido': 'ind_excluido'
        }
    },
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
        'name': '_assuntonorma',
        's30_model': _AssuntoNorma,
        's31_model': None,
        'fields': {
            '': 'cod_assunto',
            '': 'des_assunto',
                '': 'des_estendida',
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
        'name': '_comissao',
        's30_model': _Comissao,
        's31_model': None,
        'fields': {
            '': 'cod_comissao',
                '': 'tip_comissao',
                '': 'nom_comissao',
                '': 'sgl_comissao',
                '': 'dat_criacao',
                '': 'dat_extincao',
                '': 'nom_apelido_temp',
                '': 'dat_instalacao_temp',
                '': 'dat_final_prevista_temp',
                '': 'dat_prorrogada_temp',
                '': 'dat_fim_comissao',
                '': 'nom_secretario',
                '': 'num_tel_reuniao',
                '': 'end_secretaria',
                '': 'num_tel_secretaria',
                '': 'num_fax_secretaria',
                '': 'des_agenda_reuniao',
                '': 'loc_reuniao',
                '': 'txt_finalidade',
                '': 'end_email',
                '': 'ind_unid_deliberativa',
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
        'name': '_orgao',
        's30_model': _Orgao,
        's31_model': None,
        'fields': {
            '': 'cod_orgao',
            '': 'nom_orgao',
                '': 'sgl_orgao',
                '': 'ind_unid_deliberativa',
                '': 'end_orgao',
                '': 'num_tel_orgao',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_origem',
        's30_model': _Origem,
        's31_model': None,
        'fields': {
            '': 'cod_origem',
            '': 'sgl_origem',
                '': 'nom_origem',
                'ind_excluido': 'ind_excluido'
        }
    },
    {
        'name': '_parlamentar',
        's30_model': _Parlamentar,
        's31_model': None,
        'fields': {
            '': 'cod_parlamentar',
            '': 'cod_nivel_instrucao',
                '': 'tip_situacao_militar',
                '': 'nom_completo',
                '': 'nom_parlamentar',
                '': 'sex_parlamentar',
                '': 'dat_nascimento',
                '': 'num_cpf',
                '': 'num_rg',
                '': 'num_tit_eleitor',
                '': 'cod_casa',
                '': 'num_gab_parlamentar',
                '': 'num_tel_parlamentar',
                '': 'num_fax_parlamentar',
                '': 'end_residencial',
                '': 'cod_localidade_resid',
                '': 'num_cep_resid',
                '': 'num_tel_resid',
                '': 'num_fax_resid',
                '': 'end_web',
                '': 'nom_profissao',
                '': 'end_email',
                '': 'des_local_atuacao',
                '': 'ind_ativo',
                '': 'txt_biografia',
                '': 'txt_observacao',
                '': 'ind_unid_deliberativa',
                '': 'txt_login',
                'ind_excluido': 'ind_excluido'
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
