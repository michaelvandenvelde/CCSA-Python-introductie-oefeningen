aantal_appels = int(input())

appels_per_kist = 20
kisten_per_pallet = 35
appels_per_pallet = appels_per_kist * kisten_per_pallet

aantal_palletten = aantal_appels // appels_per_pallet
overgebleven_appels = aantal_appels % appels_per_pallet

aantal_kisten = overgebleven_appels // appels_per_kist
resterende_appels = overgebleven_appels % appels_per_kist

print(aantal_palletten)
print(aantal_kisten)
print(resterende_appels)
