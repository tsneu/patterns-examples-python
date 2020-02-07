
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- produto:

CREATE TABLE [dbo].[produto](
	[id_produto] [int] IDENTITY(1,1) NOT NULL,
	[descricao] [varchar](255) NOT NULL,
	[valor] [numeric](15,2) NOT NULL,
    [id_categoria] [int] NULL,
    [nome_imagem] [varchar] (100) NULL,
	[informacoes] [varchar](max) NULL,
	[situacao] [char](1) NOT NULL,
	[dt_cadastro] [datetime] NOT NULL,
	[dt_alteracao] [datetime] NULL,
 CONSTRAINT [pk_id_produto] PRIMARY KEY CLUSTERED 
(
	[id_produto] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

-- categoria

CREATE TABLE [dbo].[categoria](
	[id_categoria] [int] IDENTITY(1,1) NOT NULL,
	[descricao] [varchar](30) NOT NULL,
	[situacao] [char](1) NOT NULL,
	[dt_cadastro] [datetime] NOT NULL,
	[dt_alteracao] [datetime] NOT NULL,
 CONSTRAINT [pk_id_categoria] PRIMARY KEY CLUSTERED 
(
	[id_categoria] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO

ALTER TABLE [dbo].[produto] WITH CHECK ADD CONSTRAINT [fk_produto_categoria__id_categoria] FOREIGN KEY([id_categoria])
REFERENCES [dbo].[categoria] ([id_categoria])
GO

-- videos

CREATE TABLE [dbo].[produto_video_youtube](
	[id_video] [int] IDENTITY(1,1) NOT NULL,
	[titulo] [varchar](100) NULL,
	[link_web] [varchar](255) NULL,
	[id_produto] [int] NOT NULL
PRIMARY KEY CLUSTERED 
(
	[id_video] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 70) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO

ALTER TABLE [dbo].[produto_video_youtube] WITH CHECK ADD CONSTRAINT [fk_produto_video__id_produto] FOREIGN KEY([id_produto])
REFERENCES [dbo].[produto] ([id_produto])
GO

-- FAQ

CREATE TABLE [dbo].[Faq](
	[id_faq] [int] IDENTITY(1,1) NOT NULL,
	[nome] [varchar](100) NULL,
	[email] [varchar](100) NULL,
	[texto] [varchar](max) NULL,
	[dt_cadastro] [datetime] NULL,
	[dt_alteracao] [datetime] NULL,
	[situacao] [char](1) NULL,
	[id_produto] [int] NULL,
	[id_faq_pai] [int] NULL,
	[status] [char](1) NOT NULL,
	[cliente] [char](1) NULL,
PRIMARY KEY CLUSTERED 
(
	[id_faq] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, FILLFACTOR = 70) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

GO


EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'M - Moderação; A - Autorizado; N - Não autorizado' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Faq', @level2type=N'COLUMN',@level2name=N'status'
GO
EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'(S)im; (N)ão' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'Faq', @level2type=N'COLUMN',@level2name=N'cliente'
GO


