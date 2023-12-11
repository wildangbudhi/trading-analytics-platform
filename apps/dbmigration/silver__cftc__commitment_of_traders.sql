CREATE TABLE IF NOT EXISTS public.silver__cftc__commitment_of_traders (
    surr_key varchar primary key,
    date date,
    exchange varchar,
    data_type varchar,
    non_com_long double precision, 
    non_com_short double precision, 
    non_com_spreads double precision, 
    com_long double precision, 
    com_short double precision,
    total_long double precision, 
    total_short double precision,
    non_reportable_long double precision, 
    non_reportable_short double precision, 
    ts bigint
);

CREATE INDEX IF NOT EXISTS silver__cc__1__idx ON public.silver__cftc__commitment_of_traders(date);
CREATE INDEX IF NOT EXISTS silver__cc__2__idx ON public.silver__cftc__commitment_of_traders(exchange);
CREATE INDEX IF NOT EXISTS silver__cc__3__idx ON public.silver__cftc__commitment_of_traders(data_type);
CREATE INDEX IF NOT EXISTS silver__cc__4__idx ON public.silver__cftc__commitment_of_traders(ts);
