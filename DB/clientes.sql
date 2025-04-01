-- Table: public.Clientes

-- DROP TABLE IF EXISTS public."Clientes";

CREATE TABLE IF NOT EXISTS public."Clientes"
(
    cliente_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nombre character varying(60) COLLATE pg_catalog."default",
    edad integer,
    genero character(20) COLLATE pg_catalog."default",
    ubicacion character(25) COLLATE pg_catalog."default",
    CONSTRAINT "Clientes_pkey" PRIMARY KEY (cliente_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Clientes"
    OWNER to postgres;