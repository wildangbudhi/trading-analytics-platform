CREATE TABLE IF NOT EXISTS public.silver__dim_country_mapper (
    currency_code varchar,
    trading_economics_code varchar,
    cot_code varchar
);

CREATE INDEX IF NOT EXISTS silver__dcm__1__idx ON public.silver__dim_country_mapper(currency_code);
CREATE INDEX IF NOT EXISTS silver__dcm__2__idx ON public.silver__dim_country_mapper(trading_economics_code);
CREATE INDEX IF NOT EXISTS silver__dcm__3__idx ON public.silver__dim_country_mapper(cot_code);

INSERT INTO public.silver__dim_country_mapper
VALUES 
( 'aud', 'australia', 'AUSTRALIAN DOLLAR' ),
( 'cad', 'canada', 'CANADIAN DOLLAR' ),
( 'chf', 'switzerland', 'SWISS FRANC' ),
( 'eur', 'euro-area', 'EURO FX' ),
( 'gbp', 'united-kingdom', 'BRITISH POUND' ),
( 'jpy', 'japan', 'JAPANESE YEN' ),
( 'nzd', 'new-zealand', 'NZ DOLLAR' ),
( 'usd', 'united-states', 'USD INDEX' )
;