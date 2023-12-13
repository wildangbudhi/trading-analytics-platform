CREATE TABLE IF NOT EXISTS public.bronze__tradingeconomics__country_economics_data (
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

CREATE INDEX IF NOT EXISTS bronze__tc__1__idx ON public.bronze__tradingeconomics__country_economics_data(country_code);
CREATE INDEX IF NOT EXISTS bronze__tc__2__idx ON public.bronze__tradingeconomics__country_economics_data(category);
CREATE INDEX IF NOT EXISTS bronze__tc__3__idx ON public.bronze__tradingeconomics__country_economics_data(metrics);
CREATE INDEX IF NOT EXISTS bronze__tc__4__idx ON public.bronze__tradingeconomics__country_economics_data(last_data_date);
CREATE INDEX IF NOT EXISTS bronze__tc__5__idx ON public.bronze__tradingeconomics__country_economics_data(ts);
