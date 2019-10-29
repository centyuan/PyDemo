

"""
lottery.Setting
lottery.Species
im.GroupType
im.Group
enterprise.Domain
##enterprise.Enterprise
"""

from django.db import transaction
import lottery
import im
import enterprise

#enterprise_obj = enterprise.models.Enterprise.objects.get(id=12)
@transaction.atomic
def exe():
        enterprise_obj = enterprise.models.Enterprise.objects.get(id=13)
        for item in lottery.models.Setting.objects.filter(enterprise=7):
setting_obj = lottery.models.Setting()
setting_obj.enterprise = enterprise_obj
setting_obj.key = item.key
setting_obj.value = item.value
setting_obj.public = item.public
setting_obj.desc = item.desc
setting_obj.save()

@transaction.atomic
def exe():
    enterprise_obj = enterprise.models.Enterprise.objects.get(id=12)
    for item in lottery.models.Species.objects.filter(enterprise=5):
        species_obj = lottery.models.Species()
        species_obj.enterprise = enterprise_obj
        species_obj.name = item.name
        species_obj.code = item.code
        species_obj.countdown_threshold = item.countdown_threshold
        species_obj.server_time_offset = item.server_time_offset
        species_obj.time_offset = item.time_offset
        species_obj.in_use = item.in_use
        species_obj.rule_desc = item.rule_desc
        species_obj.imgurl = item.imgurl
        species_obj.front_cover = item.front_cover
        species_obj.opentime_desc = item.opentime_desc
        species_obj.frequency_desc = item.frequency_desc
        species_obj.bet_money = item.bet_money
        species_obj.periodnumber_limit_bonus = item.periodnumber_limit_bonus
        species_obj.single_betno_limit_bonus = item.single_betno_limit_bonus
        species_obj.single_pick_max_bonus = item.single_pick_max_bonus
        species_obj.priority = item.priority
        species_obj.is_recommend = item.is_recommend
        species_obj.type_label = item.type_label
        species_obj.type_label1 = item.type_label1
        species_obj.lucky_rate = item.lucky_rate
        species_obj.scope = item.scope
        species_obj.save()


from django_import.db import transaction
import lottery
import im
import enterprise

group = []
accounts = []
@transaction.atomic
def exe():
    enterprise_obj = enterprise.models.Enterprise.objects.get(id=13)
    for item in im.models.Group.objects.filter(enterprise=7):
    #item = im.models.Group.objects.get(id=33485)
group_obj = im.models.Group()
group_obj.enterprise = enterprise_obj
group_obj.name = item.name
group_obj.desc = item.desc
#group_obj.groupnum = item.groupnum
group_obj.group_name = item.group_name
group_obj.group_type = im.models.GroupType.objects.get(id=item.group_type.id)
#group_obj.groupmembers = item.groupmembers.all()
# for groupmem in item.groupmembers.all():
#     group_obj.groupmembers.add(groupmem)
group_obj.create_time = item.create_time
group_obj.settings = item.settings
group_obj.qrcode = item.qrcode
group_obj.openness = item.openness
group_obj.system = item.system
group_obj.front_cover = item.front_cover
group_obj.is_review = item.is_review
group_obj.sort = item.sort
group_obj.img_url = item.img_url
group_obj.group_name_title = item.group_name_title
group_obj.group_name_odd = item.group_name_odd
group_obj.passkey = item.passkey
group_obj.bulletin = item.bulletin
group_obj.ban_message = item.ban_message
group_obj.ban_speech = item.ban_speech
group_obj.invitation_confirm = item.invitation_confirm
group_obj.prize_pool = item.prize_pool
group_obj.mian_amount_dividend_rules =item.mian_amount_dividend_rules
group_obj.award_rules = item.award_rules
group_obj.homeowner_dividend_rules = item.homeowner_dividend_rules
group_obj.autu_send = item.autu_send
group_obj.autu_accept = item.autu_accept
group_obj.label = item.label
group_obj.otplaycode = item.otplaycode
group_obj.save()
for account in item.groupmembers.all():
    im.models.GroupMember.objects.create(group=group_obj,account=account)



@transaction.atomic
def exe():
    species = lottery.models.Species.objects.get(id=41)
    new_species = lottery.models.Species.objects.get(id=54)
    all_species_play = lottery.models.SpeciesPlay.objects.filter(species=species)
    for play_ in all_species_play:
play_obj = lottery.models.SpeciesPlay()
play_obj.species = new_species
play_obj.species_group = play_.species_group
play_obj.play = play_.play
play_obj.help = play_.help
play_obj.example = play_.example
play_obj.tips = play_.tips
play_obj.showname = play_.showname
play_obj.max_bonus = play_.max_bonus
play_obj.playcode = play_.playcode
play_obj.min_betno = play_.min_betno
play_obj.max_betno = play_.max_betno
play_obj.full_betno = play_.full_betno
play_obj.specialcase = play_.specialcase
play_obj.in_use = play_.in_use
play_obj.is_default = play_.is_default
play_obj.sort = play_.sort
play_obj.label = play_.label
play_obj.scope = play_.scope
play_obj.save()








