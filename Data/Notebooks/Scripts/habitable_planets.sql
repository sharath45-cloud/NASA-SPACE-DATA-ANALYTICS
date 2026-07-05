-- Table: public.habitable_planets

-- DROP TABLE IF EXISTS public.habitable_planets;

CREATE TABLE IF NOT EXISTS public.habitable_planets
(
    planet_id character varying(100) COLLATE pg_catalog."default",
    planet_name character varying(100) COLLATE pg_catalog."default",
    planet_status character varying(50) COLLATE pg_catalog."default",
    planet_size_earths numeric,
    planet_temperature_k_elvin numeric,
    orbital_period_days character varying(100) COLLATE pg_catalog."default",
    orbital_period_upper_err1 numeric,
    orbital_period_lower_err2 numeric
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.habitable_planets
    OWNER to postgres;



select*from public.habitable_planets;
