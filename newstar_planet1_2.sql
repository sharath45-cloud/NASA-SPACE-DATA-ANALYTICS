-- Table: public.newstar_planet1_2

-- DROP TABLE IF EXISTS public.newstar_planet1_2;

CREATE TABLE IF NOT EXISTS public.newstar_planet1_2
(
    planet_id text COLLATE pg_catalog."default",
    target_id text COLLATE pg_catalog."default",
    kepler_object_name text COLLATE pg_catalog."default",
    planet_name text COLLATE pg_catalog."default",
    planet_status text COLLATE pg_catalog."default",
    preliminary_status text COLLATE pg_catalog."default",
    confidence_score text COLLATE pg_catalog."default",
    flag_not_transit_like text COLLATE pg_catalog."default",
    flag_stellar_eclipse text COLLATE pg_catalog."default",
    flag_centroid_offset text COLLATE pg_catalog."default",
    flag_ephemeris_match text COLLATE pg_catalog."default",
    orbital_period_days text COLLATE pg_catalog."default",
    orbital_period_upper_err1 text COLLATE pg_catalog."default",
    orbital_period_lower_err2 text COLLATE pg_catalog."default",
    tansit_epoch_time text COLLATE pg_catalog."default",
    transit_time_upper_err1 text COLLATE pg_catalog."default",
    transit_time_lower_err2 text COLLATE pg_catalog."default",
    impact_parameter text COLLATE pg_catalog."default",
    impact_upper_err1 text COLLATE pg_catalog."default",
    impact_lower_err2 text COLLATE pg_catalog."default",
    transit_duration_hours text COLLATE pg_catalog."default",
    transit_duration_upper_err1 text COLLATE pg_catalog."default",
    transit_duration_lower_err2 text COLLATE pg_catalog."default",
    transit_depth_ppm text COLLATE pg_catalog."default",
    transit_depth_upper_err1 text COLLATE pg_catalog."default",
    transit_depth_lower_err2 text COLLATE pg_catalog."default",
    planet_size_earths numeric,
    planet_size_earths_err1 text COLLATE pg_catalog."default",
    planet_size_earths_err2 text COLLATE pg_catalog."default",
    planet_temperature_k_elvin integer,
    planet_temperature_k_elvin_err1 text COLLATE pg_catalog."default",
    planet_temperature_k_elvin_err2 text COLLATE pg_catalog."default",
    insolation_flux_earths text COLLATE pg_catalog."default",
    insolation_upper_err1 text COLLATE pg_catalog."default",
    insolation_lower_err2 text COLLATE pg_catalog."default",
    "signal _to_noise_ratio" text COLLATE pg_catalog."default",
    tec_planet_number text COLLATE pg_catalog."default",
    tce_delivery_name text COLLATE pg_catalog."default",
    "star_temperature_kelvi n" text COLLATE pg_catalog."default",
    "star_temperature_kelvi n_err1" text COLLATE pg_catalog."default",
    "star_temperature_kelvi n_err2" text COLLATE pg_catalog."default",
    star_gravity_logg text COLLATE pg_catalog."default",
    star_gravity_upper_err1 text COLLATE pg_catalog."default",
    star_gravity_lower_err2 text COLLATE pg_catalog."default",
    star_size_suns text COLLATE pg_catalog."default",
    star_size_upper_err1 text COLLATE pg_catalog."default",
    star_size_lower_err2 text COLLATE pg_catalog."default",
    sky_right_ascension text COLLATE pg_catalog."default",
    sky_declination text COLLATE pg_catalog."default",
    kepler_magnitude_brightness text COLLATE pg_catalog."default"
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.newstar_planet1_2
    OWNER to postgres;

select*from  public.newstar_planet1_2;

select*