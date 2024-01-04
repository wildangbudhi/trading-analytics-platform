CREATE TABLE IF NOT EXISTS public.silver__economics_data_weights (
    country_code varchar,
    metrics varchar,
    weight double precision,
);

CREATE INDEX IF NOT EXISTS silver__edw__1__idx ON public.silver__economics_data_weights(country_code);
CREATE INDEX IF NOT EXISTS silver__edw__2__idx ON public.silver__economics_data_weights(metrics);
CREATE INDEX IF NOT EXISTS silver__edw__3__idx ON public.silver__economics_data_weights(weight);

INSERT INTO public.silver__economics_data_weights
VALUES 
( 'australia', 'GDP Growth Rate', 2 ),
( 'australia', 'GDP Annual Growth Rate', 2 ),
( 'australia', 'Unemployment Rate', 2 ),
( 'australia', 'Inflation Rate', -2 ),
( 'australia', 'Inflation Rate MoM', -1 ),
( 'australia', 'Balance of Trade', 1 ),
( 'australia', 'Current Account', 1 ),
( 'australia', 'Current Account to GDP', 1 ),
( 'australia', 'Government Debt to GDP', 1 ),
( 'australia', 'Government Budget', 1 ),
( 'australia', 'Business Confidence', 2 ),
( 'australia', 'Manufacturing PMI', 2 ),
( 'australia', 'Services PMI', 2 ),
( 'australia', 'Consumer Confidence', 2 ),
( 'australia', 'Retail Sales MoM', 2 ),
( 'australia', 'Building Permits', 2 ),
( 'canada', 'GDP Growth Rate', 2 ),
( 'canada', 'GDP Annual Growth Rate', 2 ),
( 'canada', 'GDP Growth Annualized', 2 ),
( 'canada', 'Unemployment Rate', 2 ),
( 'canada', 'Inflation Rate', -2 ),
( 'canada', 'Inflation Rate MoM', -1 ),
( 'canada', 'Balance of Trade' , 1 ),
( 'canada', 'Current Account', 1 ),
( 'canada', 'Current Account to GDP', 1 ),
( 'canada', 'Government Debt to GDP', 1 ),
( 'canada', 'Government Budget', 1 ),
( 'canada', 'Business Confidence', 2 ),
( 'canada', 'Manufacturing PMI', 2 ),
( 'canada', 'Consumer Confidence', 2 ),
( 'canada', 'Retail Sales MoM', 2 ),
( 'canada', 'Building Permits', 2 ),
( 'switzerland', 'GDP Growth Rate', 2 ),
( 'switzerland', 'GDP Annual Growth Rate', 2 ),
( 'switzerland', 'Unemployment Rate', 2 ),
( 'switzerland', 'Inflation Rate', -2 ),
( 'switzerland', 'Inflation Rate MoM', -1 ),
( 'switzerland', 'Balance of Trade', 1 ),
( 'switzerland', 'Current Account', 1 ),
( 'switzerland', 'Current Account to GDP', 1 ),
( 'switzerland', 'Government Debt to GDP', 1 ),
( 'switzerland', 'Government Budget', 1 ),
( 'switzerland', 'Business Confidence', 2 ),
( 'switzerland', 'Manufacturing PMI', 2 ),
( 'switzerland', 'Consumer Confidence', 2 ),
( 'switzerland', 'Retail Sales MoM', 2 ),
( 'euro-area', 'GDP Growth Rate', 2 ),
( 'euro-area', 'GDP Annual Growth Rate', 2 ),
( 'euro-area', 'Unemployment Rate', 2 ),
( 'euro-area', 'Inflation Rate', -2 ),
( 'euro-area', 'Inflation Rate MoM', -1 ),
( 'euro-area', 'Balance of Trade', 1 ),
( 'euro-area', 'Current Account', 1 ),
( 'euro-area', 'Current Account to GDP', 1 ),
( 'euro-area', 'Government Debt to GDP', 1 ),
( 'euro-area', 'Government Budget', 1 ),
( 'euro-area', 'Business Confidence', 2 ),
( 'euro-area', 'Manufacturing PMI', 2 ),
( 'euro-area', 'Services PMI', 2 ),
( 'euro-area', 'Consumer Confidence', 2 ),
( 'euro-area', 'Retail Sales MoM', 2 ),
( 'united-kingdom', 'GDP Growth Rate', 2 ),
( 'united-kingdom', 'GDP Annual Growth Rate', 2 ),
( 'united-kingdom', 'Unemployment Rate', 2 ),
( 'united-kingdom', 'Inflation Rate', -2 ),
( 'united-kingdom', 'Inflation Rate MoM', -1 ),
( 'united-kingdom', 'Balance of Trade', 1 ),
( 'united-kingdom', 'Current Account', 1 ),
( 'united-kingdom', 'Current Account to GDP', 1 ),
( 'united-kingdom', 'Government Debt to GDP', 1 ),
( 'united-kingdom', 'Government Budget', 1 ),
( 'united-kingdom', 'Business Confidence', 2 ),
( 'united-kingdom', 'Manufacturing PMI', 2 ),
( 'united-kingdom', 'Services PMI', 2 ),
( 'united-kingdom', 'Consumer Confidence', -2 ),
( 'united-kingdom', 'Retail Sales MoM', 2 ),
( 'japan', 'GDP Growth Rate', 2 ),
( 'japan', 'GDP Annual Growth Rate', 2 ),
( 'japan', 'GDP Growth Annualized', 2 ),
( 'japan', 'Unemployment Rate', 2 ),
( 'japan', 'Inflation Rate', 2 ),
( 'japan', 'Inflation Rate MoM', 1 ),
( 'japan', 'Balance of Trade', 1 ),
( 'japan', 'Current Account', 1 ),
( 'japan', 'Current Account to GDP', 1 ),
( 'japan', 'Government Debt to GDP', 1 ),
( 'japan', 'Government Budget', 1 ),
( 'japan', 'Business Confidence', 2 ),
( 'japan', 'Manufacturing PMI', 2 ),
( 'japan', 'Services PMI', 2 ),
( 'japan', 'Consumer Confidence', 2 ),
( 'japan', 'Retail Sales MoM', 2 ),
( 'new-zealand', 'GDP Growth Rate', 2 ),
( 'new-zealand', 'GDP Annual Growth Rate', 2 ),
( 'new-zealand', 'Unemployment Rate', 2 ),
( 'new-zealand', 'Inflation Rate', -2 ),
( 'new-zealand', 'Inflation Rate MoM', -1 ),
( 'new-zealand', 'Balance of Trade', 1 ),
( 'new-zealand', 'Current Account', 1 ),
( 'new-zealand', 'Current Account to GDP', 1 ),
( 'new-zealand', 'Government Debt to GDP', 1 ),
( 'new-zealand', 'Government Budget', 1 ),
( 'new-zealand', 'Business Confidence', 2 ),
( 'new-zealand', 'Manufacturing PMI', 2 ),
( 'new-zealand', 'Consumer Confidence', 2 ),
( 'new-zealand', 'Retail Sales MoM', 2 ),
( 'new-zealand', 'Building Permits', 2 ),
( 'united-states', 'GDP Growth Rate', 2 ),
( 'united-states', 'GDP Annual Growth Rate', 2 ),
( 'united-states', 'Unemployment Rate', 2 ),
( 'united-states', 'Non Farm Payrolls', 2 ),
( 'united-states', 'Inflation Rate', -2 ),
( 'united-states', 'Inflation Rate MoM', -1 ),
( 'united-states', 'Balance of Trade', 1 ),
( 'united-states', 'Current Account', 1 ),
( 'united-states', 'Current Account to GDP', 1 ),
( 'united-states', 'Government Debt to GDP', 1 ),
( 'united-states', 'Government Budget', 1 ),
( 'united-states', 'Business Confidence', 2 ),
( 'united-states', 'Manufacturing PMI', 2 ),
( 'united-states', 'Non Manufacturing PMI', 2 ),
( 'united-states', 'Services PMI', 2 ),
( 'united-states', 'Consumer Confidence', 2 ),
( 'united-states', 'Retail Sales MoM', 2 ),
( 'united-states', 'Building Permits', 2 )
;