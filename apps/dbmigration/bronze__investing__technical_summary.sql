CREATE TABLE IF NOT EXISTS public.bronze__investing__technical_summary (
    pair varchar,
    hourly varchar,
    daily varchar,
    weekly varchar,
    monthly varchar,
    ts bigint
);

CREATE INDEX IF NOT EXISTS bronze__it__1__idx ON public.bronze__investing__technical_summary(pair);
CREATE INDEX IF NOT EXISTS bronze__it__2__idx ON public.bronze__investing__technical_summary(ts);
