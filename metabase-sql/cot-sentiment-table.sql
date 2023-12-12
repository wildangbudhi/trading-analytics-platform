with cot_ as (
    select 
            date
        , exchange
        , (non_com_long - non_com_short) as sentiment
    from 
        public.silver__cftc__commitment_of_traders
    where 
        data_type = 'COMMITMENTS'
        and exchange in (
            'CANADIAN DOLLAR',
            'SWISS FRANC',
            'BRITISH POUND',
            'AUSTRALIAN DOLLAR',
            'NZ DOLLAR',
            'JAPANESE YEN',
            'EURO FX',
            'USD INDEX'
        )
)

, cot_changes_ as (
    select 
            date
        , exchange
        , (non_com_long - non_com_short) as sentiment
        , row_number() over (partition by date, exchange order by ts desc) as rn
    from 
        public.silver__cftc__commitment_of_traders
    where 
        data_type = 'CHANGES'
        and exchange in (
            'CANADIAN DOLLAR',
            'SWISS FRANC',
            'BRITISH POUND',
            'AUSTRALIAN DOLLAR',
            'NZ DOLLAR',
            'JAPANESE YEN',
            'EURO FX',
            'USD INDEX'
        )
)

, sentiment_data as (
    select 
        a.date,
        a.exchange,
        a.sentiment as cot_sentiment,
        b.sentiment as cot_change_sentiment
    from 
        cot_ a
    left join
        cot_changes_ b
        on a.date = b.date
        and a.exchange = b.exchange
)

select  
    a.date,
    a.exchange as exchange_a,
    b.exchange as exchange_b,
    a.cot_sentiment as cot_sentiment_a,
    b.cot_sentiment as cot_sentiment_b,
    a.cot_change_sentiment as cot_change_sentiment_a,
    b.cot_change_sentiment as cot_change_sentiment_b,
    (a.cot_sentiment - b.cot_sentiment) as pair_cot_sentiment,
    (a.cot_change_sentiment - b.cot_change_sentiment) as pair_cot_changes_sentiment
from 
    sentiment_data a
left join
    sentiment_data b
    on a.date = b.date
where
    a.exchange <> b.exchange
order by
    8 DESC, 9 DESC