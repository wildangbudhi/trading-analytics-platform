CREATE TABLE IF NOT EXISTS public.silver__tradingeconomics__country_economics_data (
    surr_key varchar primary key,
    country_code varchar,
    category varchar,
    metrics varchar,
    last double precision,
    previous double precision,
    highest double precision,
    lowest double precision,
    unit varchar,
    last_data_date date,
    ts bigint
);

CREATE INDEX IF NOT EXISTS silver__tc__1__idx ON public.silver__tradingeconomics__country_economics_data(country_code);
CREATE INDEX IF NOT EXISTS silver__tc__2__idx ON public.silver__tradingeconomics__country_economics_data(category);
CREATE INDEX IF NOT EXISTS silver__tc__3__idx ON public.silver__tradingeconomics__country_economics_data(metrics);
CREATE INDEX IF NOT EXISTS silver__tc__4__idx ON public.silver__tradingeconomics__country_economics_data(last_data_date);
CREATE INDEX IF NOT EXISTS silver__tc__5__idx ON public.silver__tradingeconomics__country_economics_data(ts);
