import pandas as pd


MAX_COLS = {
    'Symptomatic isolation - targeted':{'contact isolation - symptoms':1,
                                        'cohort isolation - symptoms':1},
    'Symptomatic isolation - blanket':{'cluster isolation - symptoms':1,
                                       'blanket isolation - symptoms':2},
    'Asymptomatic isolation - targeted':{'contact isolation - no symptoms':1,
                                         'cohort isolation - no symptoms':2},
    'Asymptomatic isolation - blanket':{'cluster isolation - no symptoms':1,
                                        'blanket isolation - no symptoms':3,
                                        'blanket curfew - no symptoms':2,
                                        'natural village quarantine':3},
    'Domestic travel restriction':{'domestic traveller quarantine':1,
                                   'domestic travel ban':2,
                                   'total vehicle ban':2},
    'Nonessential business suspension':{'general nonessential business suspension':1,
                                        'limited nonessential business suspension':0.5,
                                   'remote work':0.5},
    'International travel restriction':{'international traveller screening - risk countries':1,
                                        'international traveller screening - all countries':2,
                                        'international traveller quarantine - risk countries':3,
                                        'international traveller quarantine - all countries':4,
                                        'international travel ban - risk countries':5,
                                        'international travel ban - all countries':6},
    'Testing':{'testing numbers total':np.nan},
    'Contact tracing':{'contacts traced total':np.nan},
    'Mask wearing':{'public mask wearing data':np.nan},
    'Hand washing':{'public handwashing data':np.nan}
    
}

MIN_COLS = {
    'Gatherings banned':['indoor gatherings banned',
                        'outdoor gatherings banned']
}

CUMSUM_COLS = {
    'Healthcare specialisation':['clinic specialisation',
                                'case transport',
                                'quarantine zone',
                                'hospital specialisation',
                                'healthcare entry screening',
                                'remote medical treatment',
                                'visiting in hospital banned'],
    'Public education and incentives':['risk communication',
                                      'community engagement',
                                      'coronavirus education activities',
                                      'phone line'],
    'Assisting people to stay home':['unemployment benefits extension',
                                    'eviction moratorium',
                                    'isolation allowance',
                                    'compulsory isolation'],
    'Public cleaning':['public transport cleaning',
                      'public facility cleaning'],
    'Miscellaneous hygiene measures':['funeral hygiene',
                                     'cash cleaning',
                                     'cash banned'],
    'Public interaction and hygiene':['handshakes banned',
                                    'social distancing advice',
                                    'stay home advice',
                                    'space minimum',
                                    'outdoor person density',
                                    'indoor person density',
                                    'public venue screening',
                                    'handwashing encouragement',
                                    'public mask encouragement',
                                    'public mask supply',
                                    'public mask and hygiene supply',
                                    'public hand sanitizer supply'],
    'School closure':['school closure',
                     'university closure',
                     'nursery school closure',
                     'remote schooling',
                     'public transport stopped'],
    'Activity cancellation':['activity cancellation - other',
                            'sports cancellation',
                            'religious activity cancellation',
                            'religious activity limitations',
                            'weddings canceled',
                            'very large event cancellation or postponement',
                            'cultural activity limitation',
                            'remote cultural content',
                            'restaurant limitations',
                            'closure of gathering places'],
    'Resumption':['public transport resumed',
                 'activity resumed',
                 'business resumed'],
    'Diagnostic criteria loosened':['diagnostic criteria loosened'],
    'Diagnostic criteria tightened':['diagnostic criteria tightened']    
}

TEST_COLS = {    
    'Testing criteria':{'test all':1,
                       'test symptomatic':0.5,
                       'cluster testing':0.3,
                       'test contacts':0.1,
                       'test cohorts':0.2,
                       'test travellers':0.1,
                       'test medical staff':0.1,
                       'test vulnerable':0.1}
}


def default_values(kw):
    for k, v in {**MAX_COLS,**TEST_COLS}.items():
        if (kw in v) and (v[kw]!=np.nan):
            return v[kw]
    return np.nan


def keywords(kws_quants):
    res =  pd.DataFrame([(i,j[1]) 
                         for j in kws_quants.values 
                         for i in str(j[0]).split(', ')],
                        columns=['Keywords','Quantity'])
    res['Quantity'] = res['Keywords'].apply(default_values).fillna(res['Quantity'])
    return res