-- Table: public.Productos

-- DROP TABLE IF EXISTS public."Productos";

CREATE TABLE IF NOT EXISTS public."Productos"
(
    producto_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nombre_producto character varying(60) COLLATE pg_catalog."default",
    "categoria " character(30) COLLATE pg_catalog."default",
    precio_base money,
    CONSTRAINT "Productos_pkey" PRIMARY KEY (producto_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Productos"
    OWNER to postgres;