-- Table: public.Ventas

-- DROP TABLE IF EXISTS public."Ventas";

CREATE TABLE IF NOT EXISTS public."Ventas"
(
    venta_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    fecha date,
    producto_id integer,
    cantidad integer,
    precio_unitario money,
    cliente_id integer,
    sucursal_id integer,
    total money,
    CONSTRAINT "Ventas_pkey" PRIMARY KEY (venta_id),
    CONSTRAINT cliente_id_fkey FOREIGN KEY (cliente_id)
        REFERENCES public."Clientes" (cliente_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT producto_id_fkey FOREIGN KEY (producto_id)
        REFERENCES public."Productos" (producto_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."Ventas"
    OWNER to postgres;