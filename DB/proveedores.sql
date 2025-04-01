-- Table: public.Proveedores

-- DROP TABLE IF EXISTS public."Proveedores";

CREATE TABLE IF NOT EXISTS public."Proveedores"
(
    proveedor_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    nombre_proveedor character(70) COLLATE pg_catalog."default",
    contacto character varying(70) COLLATE pg_catalog."default",
    ubicacion character(60) COLLATE pg_catalog."default",
    CONSTRAINT "Proveedores_pkey" PRIMARY KEY (proveedor_id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Proveedores"
    OWNER to postgres;