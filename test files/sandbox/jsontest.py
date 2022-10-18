import json

globalTimeFactor = 0.85

desiredsongid = 'pentiment'
with open('410songlist.json') as f:
    with open('tempochangedsonglist.json', 'w') as newtempjson:
        data = json.load(f)
        for songid in range(len(data['songs'])):
            if desiredsongid in json.dumps(data['songs'][songid]):
                data['songs'][songid]['id'] = desiredsongid + f'{globalTimeFactor:.2f}'.replace('.','')
                data['songs'][songid]['title_localized']['en'] = data['songs'][songid]['title_localized']['en'] + f' x{globalTimeFactor:.2f}'
                try:
                    data['songs'][songid]['title_localized']['ja'] = data['songs'][songid]['title_localized']['ja'] + f' x{globalTimeFactor:.2f}'
                except:
                    pass

                if (data['songs'][songid]['bpm']).isdigit():
                    data['songs'][songid]['bpm'] = str(int(data['songs'][songid]['bpm']) * globalTimeFactor)
                    
                elif '-' in data['songs'][songid]['bpm']:
                    bpm = data['songs'][songid]['bpm'].split('-')
                    data['songs'][songid]['bpm'] = str(int(bpm[0]) * globalTimeFactor) + '-' + str(int(bpm[1]) * globalTimeFactor)

                data['songs'][songid]['purchase'] = ''
                try:
                    data['songs'][songid]['remote_dl'] = False
                except:
                    pass
                try:
                    data['songs'][songid]['world_unlock'] = False
                except:
                    pass
                try:
                    data['songs'][songid]['byd_local_unlock'] = True
                except:
                    pass


                data['songs'][songid]['bpm_base'] = data['songs'][songid]['bpm_base'] * globalTimeFactor
                new_json_formatted = json.dumps(data['songs'][songid], indent=2, ensure_ascii=False)
                newtempjson.write(new_json_formatted)


