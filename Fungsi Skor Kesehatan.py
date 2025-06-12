def infer_health_score_pmk(age, gender,
                           energy_kcal, protein_g, fat_g,
                           carb_g, fiber_g):


    akg_table = {
        'male':   {'energy': 2650, 'protein': 65, 'fat': 75, 'carb': 430, 'fiber': 37},
        'female': {'energy': 2250, 'protein': 60, 'fat': 65, 'carb': 360, 'fiber': 32},
    }

   
    grp = 'male' if gender.lower()=='male' else 'female'
    rec = akg_table[grp]

    
    r_energy  = min(energy_kcal  / rec['energy'],  1.0)
    r_protein = min(protein_g     / rec['protein'], 1.0)
    r_fat     = min(fat_g         / rec['fat'],     1.0)
    r_carb    = min(carb_g        / rec['carb'],    1.0)
    r_fiber   = min(fiber_g       / rec['fiber'],   1.0)

   
    avg_ratio = (r_energy + r_protein + r_fat + r_carb + r_fiber) / 5

   
    score = int(avg_ratio * 9) + 1
    return max(1, min(score, 10))


score = infer_health_score_pmk(
    age=25, gender='male',
    energy_kcal=2400, protein_g=55,
    fat_g=60, carb_g=400, fiber_g=30
)
print(score)