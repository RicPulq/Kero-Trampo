from app import db

__all__ = [
    "Historico_da_fabrica",
    "Piquete",
    "Historico_de_lote",
    "Historico_de_consumo_lote",
    "Batida",
    "Insumo_entrada",
    "Historico_de_residuo_de_batida",
    "Insumo_saida",
    "Imagem_da_distribuicao",
    "Insumo",
    "Composicao_da_receita",
    "Historico_de_batidas_de_confinamento",
    "Receita",
    "Batida_agendada",
    "Image",
    "Imagem_de_residuo",
    "Agenda_de_batidas",
    "Lote",
    "Saca",
    "Historico_de_insumos_por_batida"
]


class Historico_da_fabrica(db.Base):
    nro_sacas = db.Column(db.Integer, nullable=False, default=0)
    batida_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida.uuid"))
    agenda_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida_agendada.uuid"))
    observacoes = db.Column(db.String, nullable=True)
    batida_rel = db.relationship("Batida", back_populates="historico_da_fabrica_rel")
    batida_agendada_rel = db.relationship(
        "Batida_agendada", back_populates="historico_da_fabrica_rel"
    )
    saca_rel = db.relationship("Saca", back_populates="historico_da_fabrica_rel")


class Piquete(db.Base):
    area = db.Column(db.Float, nullable=False, default=0)
    lotacao_maxima = db.Column(db.Integer, nullable=False, default=0)
    comprimento_do_cocho = db.Column(db.Float, nullable=False, default=0)
    qrcode = db.Column(db.String, nullable=False, default="--")
    coordenadas = db.Column(db.String, nullable=False, default="--")
    observacoes = db.Column(db.String, nullable=True)
    historico_de_consumo_lote_rel = db.relationship(
        "Historico_de_consumo_lote", back_populates="piquete_rel"
    )


class Historico_de_lote(db.Base):
    lote_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("lote.uuid"))
    peso = db.Column(db.Float, nullable=False, default=0)
    dia_data = db.Column(db.String, nullable=False, default="--")
    nro_de__cabecas = db.Column(db.Integer, nullable=False, default=0)
    observacoes = db.Column(db.String, nullable=True)
    lote_rel = db.relationship("Lote", back_populates="historico_de_lote_rel")
    historico_de_consumo_lote_rel = db.relationship(
        "Historico_de_consumo_lote", back_populates="historico_de_lote_rel"
    )


class Historico_de_consumo_lote(db.Base):
    hist_de_lote_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("historico_de_lote.uuid"))
    coletivo_fk = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("historico_de_batidas_de_confinamento.uuid")
    )
    piquete_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("piquete.uuid"))
    historico_de_lote_rel = db.relationship(
        "Historico_de_lote", back_populates="historico_de_consumo_lote_rel"
    )
    historico_de_batidas_de_confinamento_rel = db.relationship(
        "Historico_de_batidas_de_confinamento",
        back_populates="historico_de_consumo_lote_rel",
    )
    piquete_rel = db.relationship(
        "Piquete", back_populates="historico_de_consumo_lote_rel"
    )


class Batida(db.Base):
    data_da_batida = db.Column(db.String, nullable=False, default="--")
    hora_da_batida = db.Column(db.String, nullable=False, default="--")
    peso = db.Column(db.Float, nullable=False, default=0)
    batida_agendada_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida_agendada.uuid"))
    observacoes = db.Column(db.String, nullable=True)
    historico_da_fabrica_rel = db.relationship(
        "Historico_da_fabrica", back_populates="batida_rel"
    )
    batida_agendada_rel = db.relationship(
        "Batida_agendada", back_populates="batida_rel"
    )
    historico_de_residuo_de_batida_rel = db.relationship(
        "Historico_de_residuo_de_batida", back_populates="batida_rel"
    )
    historico_de_batidas_de_confinamento_rel = db.relationship(
        "Historico_de_batidas_de_confinamento", back_populates="batida_rel"
    )
    historico_de_insumos_por_batida_rel = db.relationship(
        "Historico_de_insumos_por_batida", back_populates="batida_rel"
    )


# class User(db.Base):
#     name = db.Column(db.String, nullable=False, default="--")
#     nivel_de_acesso = db.Column(db.Integer, nullable=False, default=0)
#     email = db.Column(db.String, nullable=False, default="--")
#     password = db.Column(db.String, nullable=False, default="--")


class Insumo_entrada(db.Base):
    insumo_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("insumo.uuid"))
    data_de_compra = db.Column(db.String, nullable=False, default="--")
    quantidade = db.Column(db.Float, nullable=False, default=0)
    observacoes = db.Column(db.String, nullable=True)
    insumo_rel = db.relationship("Insumo", back_populates="insumo_entrada_rel")


class Historico_de_residuo_de_batida(db.Base):
    data_residuo = db.Column(db.String, nullable=False, default="--")
    hora_residuo = db.Column(db.String, nullable=False, default="--")
    peso_residual = db.Column(db.Float, nullable=False, default=0)
    batida_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida.uuid"))
    destino = db.Column(db.String, nullable=False, default="--")
    observacoes = db.Column(db.String, nullable=True)
    batida_rel = db.relationship(
        "Batida", back_populates="historico_de_residuo_de_batida_rel"
    )
    imagem_de_residuo_rel = db.relationship(
        "Imagem_de_residuo", back_populates="historico_de_residuo_de_batida_rel"
    )


class Insumo_saida(db.Base):
    quantidade_disponivel_receita = db.Column(db.Float, nullable=False, default=0)
    quantidade_disponivel_batida = db.Column(db.Float, nullable=False, default=0)
    observacoes = db.Column(db.String, nullable=True)
    data = db.Column(db.String, nullable=False, default="--")
    insumo_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("insumo.uuid"))
    insumo_rel = db.relationship("Insumo", back_populates="insumo_saida_rel")
    composicao_da_receita_rel = db.relationship(
        "Composicao_da_receita", back_populates="insumo_saida_rel"
    )
    historico_de_insumos_por_batida_rel = db.relationship(
        "Historico_de_insumos_por_batida", back_populates="insumo_saida_rel"
    )


class Imagem_da_distribuicao(db.Base):
    img_distribuicao_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("image.uuid"))
    distribuicao_fk = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("historico_de_batidas_de_confinamento.uuid")
    )
    image_rel = db.relationship("Image", back_populates="imagem_da_distribuicao_rel")
    historico_de_batidas_de_confinamento_rel = db.relationship(
        "Historico_de_batidas_de_confinamento",
        back_populates="imagem_da_distribuicao_rel",
    )


class Insumo(db.Base):
    nome = db.Column(db.String, nullable=False, default="--")
    observacoes = db.Column(db.String, nullable=True)
    data_de_cadastro = db.Column(db.String, nullable=False, default="--")
    insumo_entrada_rel = db.relationship("Insumo_entrada", back_populates="insumo_rel")
    insumo_saida_rel = db.relationship("Insumo_saida", back_populates="insumo_rel")


class Composicao_da_receita(db.Base):
    quantidade = db.Column(db.Float, nullable=False, default=0)
    insumos_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("insumo_saida.uuid"))
    receita_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("receita.uuid"))
    observacoes = db.Column(db.String, nullable=True)
    insumo_saida_rel = db.relationship(
        "Insumo_saida", back_populates="composicao_da_receita_rel"
    )
    receita_rel = db.relationship("Receita", back_populates="composicao_da_receita_rel")


class Historico_de_batidas_de_confinamento(db.Base):
    batida_para_confinamento_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida.uuid"))
    dia_data = db.Column(db.String, nullable=False, default="--")
    observacoes = db.Column(db.String, nullable=True)
    historico_de_consumo_lote_rel = db.relationship(
        "Historico_de_consumo_lote",
        back_populates="historico_de_batidas_de_confinamento_rel",
    )
    imagem_da_distribuicao_rel = db.relationship(
        "Imagem_da_distribuicao",
        back_populates="historico_de_batidas_de_confinamento_rel",
    )
    batida_rel = db.relationship(
        "Batida", back_populates="historico_de_batidas_de_confinamento_rel"
    )


class Receita(db.Base):
    codigo = db.Column(db.String, nullable=False, default="--")
    autor = db.Column(db.String, nullable=False, default="--")
    data_da_receita = db.Column(db.String, nullable=False, default="--")
    estado = db.Column(db.Integer, nullable=False, default=0)
    peso = db.Column(db.Float, nullable=False, default=0)
    observacoes = db.Column(db.String, nullable=True)
    composicao_da_receita_rel = db.relationship(
        "Composicao_da_receita", back_populates="receita_rel"
    )
    agenda_de_batidas_rel = db.relationship(
        "Agenda_de_batidas", back_populates="receita_rel"
    )
    saca_rel = db.relationship("Saca", back_populates="receita_rel")


class Batida_agendada(db.Base):
    destino_da_receita = db.Column(db.String, nullable=False, default="--")
    data_da_batida = db.Column(db.String, nullable=False, default="--")
    hora_da_batida = db.Column(db.String, nullable=False, default="--")
    receita_processada = db.Column(db.Integer, nullable=False, default=0)
    vagao = db.Column(db.Integer, nullable=False, default=0)
    trator = db.Column(db.Integer, nullable=False, default=0)
    colaborador = db.Column(db.String, nullable=False, default="--")
    parcetual = db.Column(db.Float, nullable=False, default=0)
    observacoes = db.Column(db.String, nullable=True)
    historico_da_fabrica_rel = db.relationship(
        "Historico_da_fabrica", back_populates="batida_agendada_rel"
    )
    batida_rel = db.relationship("Batida", back_populates="batida_agendada_rel")
    imagem_de_residuo_rel = db.relationship(
        "Imagem_de_residuo", back_populates="batida_agendada_rel"
    )
    agenda_de_batidas_rel = db.relationship(
        "Agenda_de_batidas", back_populates="batida_agendada_rel"
    )


class Image(db.Base):
    file = db.Column(db.String, nullable=False, default="--")
    tipo = db.Column(db.Integer, nullable=False, default=0)
    observacoes = db.Column(db.String, nullable=True)
    imagem_da_distribuicao_rel = db.relationship(
        "Imagem_da_distribuicao", back_populates="image_rel"
    )
    imagem_de_residuo_rel = db.relationship(
        "Imagem_de_residuo", back_populates="image_rel"
    )


class Imagem_de_residuo(db.Base):
    historico_de_residuo_de_batida_fk = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("historico_de_residuo_de_batida.uuid")
    )
    imagem_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("image.uuid"))
    imagem_para_agendar_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida_agendada.uuid"))
    historico_de_residuo_de_batida_rel = db.relationship(
        "Historico_de_residuo_de_batida", back_populates="imagem_de_residuo_rel"
    )
    image_rel = db.relationship("Image", back_populates="imagem_de_residuo_rel")
    batida_agendada_rel = db.relationship(
        "Batida_agendada", back_populates="imagem_de_residuo_rel"
    )


class Agenda_de_batidas(db.Base):
    batida_agendada_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida_agendada.uuid"))
    receita_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("receita.uuid"))
    batida_agendada_rel = db.relationship(
        "Batida_agendada", back_populates="agenda_de_batidas_rel"
    )
    receita_rel = db.relationship("Receita", back_populates="agenda_de_batidas_rel")


class Lote(db.Base):
    tipo_lote = db.Column(db.Integer, nullable=False, default=0)
    data_de_entrada = db.Column(db.String, nullable=False, default="--")
    peso_entrada = db.Column(db.Float, nullable=False, default=0)
    data_saida = db.Column(db.String, nullable=False, default="--")
    peso_saida = db.Column(db.Float, nullable=False, default=0)
    observacoes = db.Column(db.String, nullable=True)
    historico_de_lote_rel = db.relationship(
        "Historico_de_lote", back_populates="lote_rel"
    )


class Saca(db.Base):
    etiqueta = db.Column(db.String, nullable=False, default="--")
    receita_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("receita.uuid"))
    peso = db.Column(db.Float, nullable=False, default=0)
    fabricacao_data = db.Column(db.String, nullable=False, default="--")
    validade_data = db.Column(db.String, nullable=False, default="--")
    historico_de_fabrica_fk = db.Column(
        db.UUID(as_uuid=True), db.ForeignKey("historico_da_fabrica.uuid")
    )
    qrcode = db.Column(db.String, nullable=False, default="--")
    observacoes = db.Column(db.String, nullable=True)
    receita_rel = db.relationship("Receita", back_populates="saca_rel")
    historico_da_fabrica_rel = db.relationship(
        "Historico_da_fabrica", back_populates="saca_rel"
    )


class Historico_de_insumos_por_batida(db.Base):
    insumo_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("insumo_saida.uuid"))
    peso_do_insumo_no_vagao = db.Column(db.Float, nullable=False, default=0)
    batida_fk = db.Column(db.UUID(as_uuid=True), db.ForeignKey("batida.uuid"))
    observacoes = db.Column(db.String, nullable=True)
    insumo_saida_rel = db.relationship(
        "Insumo_saida", back_populates="historico_de_insumos_por_batida_rel"
    )
    batida_rel = db.relationship(
        "Batida", back_populates="historico_de_insumos_por_batida_rel"
    )
