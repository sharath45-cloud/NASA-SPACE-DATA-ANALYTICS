-- View: public.v_top_habitable_candidates

-- DROP VIEW public.v_top_habitable_candidates;

CREATE OR REPLACE VIEW public.v_top_habitable_candidates
 AS
 SELECT planet_id,
    planet_name,
    planet_status,
    planet_size_earths,
    planet_temperature_k_elvin
   FROM habitable_planets
  WHERE planet_status::text = 'CONFIRMED'::text AND planet_size_earths >= 0.8 AND planet_size_earths <= 1.5
  ORDER BY planet_size_earths;

ALTER TABLE public.v_top_habitable_candidates
    OWNER TO postgres;

