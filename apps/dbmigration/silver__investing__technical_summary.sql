CREATE TABLE IF NOT EXISTS public.silver__investing__technical_summary (
    surr_key varchar primary key,
    pair varchar,
    hourly varchar,
    daily varchar,
    weekly varchar,
    monthly varchar,
    ts bigint
);

CREATE INDEX IF NOT EXISTS silver__it__1__idx ON public.silver__investing__technical_summary(date);
CREATE INDEX IF NOT EXISTS silver__it__2__idx ON public.silver__investing__technical_summary(ts);
