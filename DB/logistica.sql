-- Table: public.Logistica

-- DROP TABLE IF EXISTS public."Logistica";

CREATE TABLE IF NOT EXISTS public."Logistica"
(
    envio_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    venta_id integer,
    fecha_envio date,
    proveedor_id integer,
    estado_envio character(30) COLLATE pg_catalog."default",
    CONSTRAINT "Logistica_pkey" PRIMARY KEY (envio_id),
    CONSTRAINT proveedor_id_fkey FOREIGN KEY (proveedor_id)
        REFERENCES public."Proveedores" (proveedor_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT venta_id_fkey FOREIGN KEY (venta_id)
        REFERENCES public."Ventas" (venta_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Logistica"
    OWNER to postgres;