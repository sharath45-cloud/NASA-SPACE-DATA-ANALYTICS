-- View: public.v_planet_size_classification

-- DROP VIEW public.v_planet_size_classification;

CREATE OR REPLACE VIEW public.v_planet_size_classification
 AS
 SELECT planet_id,
    planet_name,
    planet_size_earths,
        CASE
            WHEN planet_size_earths < 0.8 THEN 'Sub-Earth'::text
            WHEN planet_size_earths >= 0.8 AND planet_size_earths <= 1.2 THEN 'Earth-size'::text
            WHEN planet_size_earths >= 1.2 AND planet_size_earths <= 2.0 THEN 'Super-Earth'::text
            ELSE 'Gas Giant CONFIRMED'::text
        END AS planet_type
   FROM habitable_planets;

ALTER TABLE public.v_planet_size_classification
    OWNER TO postgres;

