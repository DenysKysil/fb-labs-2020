#! /usr/bin/env python
# -*- coding: utf-8 -*-
import math, operator
from collections import Counter,OrderedDict

bigrams_to_num = {'аа': 0, 'аб': 1, 'ав': 2, 'аг': 3, 'ад': 4, 'ае': 5, 'аж': 6, 'аз': 7, 'аи': 8, 'ай': 9, 'ак': 10, 'ал': 11, 'ам': 12, 'ан': 13, 'ао': 14, 'ап': 15, 'ар': 16, 'ас': 17, 'ат': 18, 'ау': 19, 'аф': 20, 'ах': 21, 'ац': 22, 'ач': 23, 'аш': 24, 'ащ': 25, 'аь': 26, 'аы': 27, 'аэ': 28, 'аю': 29, 'ая': 30, 'ба': 31, 'бб': 32, 'бв': 33, 'бг': 34, 'бд': 35, 'бе': 36, 'бж': 37, 'бз': 38, 'би': 39, 'бй': 40, 'бк': 41, 'бл': 42, 'бм': 43, 'бн': 44, 'бо': 45, 'бп': 46, 'бр': 47, 'бс': 48, 'бт': 49, 'бу': 50, 'бф': 51, 'бх': 52, 'бц': 53, 'бч': 54, 'бш': 55, 'бщ': 56, 'бь': 57, 'бы': 58, 'бэ': 59, 'бю': 60, 'бя': 61, 'ва': 62, 'вб': 63, 'вв': 64, 'вг': 65, 'вд': 66, 'ве': 67, 'вж': 68, 'вз': 69, 'ви': 70, 'вй': 71, 'вк': 72, 'вл': 73, 'вм': 74, 'вн': 75, 'во': 76, 'вп': 77, 'вр': 78, 'вс': 79, 'вт': 80, 'ву': 81, 'вф': 82, 'вх': 83, 'вц': 84, 'вч': 85, 'вш': 86, 'вщ': 87, 'вь': 88, 'вы': 89, 'вэ': 90, 'вю': 91, 'вя': 92, 'га': 93, 'гб': 94, 'гв': 95, 'гг': 96, 'гд': 97, 'ге': 98, 'гж': 99, 'гз': 100, 'ги': 101, 'гй': 102, 'гк': 103, 'гл': 104, 'гм': 105, 'гн': 106, 'го': 107, 'гп': 108, 'гр': 109, 'гс': 110, 'гт': 111, 'гу': 112, 'гф': 113, 'гх': 114, 'гц': 115, 'гч': 116, 'гш': 117, 'гщ': 118, 'гь': 119, 'гы': 120, 'гэ': 121, 'гю': 122, 'гя': 123, 'да': 124, 'дб': 125, 'дв': 126, 'дг': 127, 'дд': 128, 'де': 129, 'дж': 130, 'дз': 131, 'ди': 132, 'дй': 133, 'дк': 134, 'дл': 135, 'дм': 136, 'дн': 137, 'до': 138, 'дп': 139, 'др': 140, 'дс': 141, 'дт': 142, 'ду': 143, 'дф': 144, 'дх': 145, 'дц': 146, 'дч': 147, 'дш': 148, 'дщ': 149, 'дь': 150, 'ды': 151, 'дэ': 152, 'дю': 153, 'дя': 154, 'еа': 155, 'еб': 156, 'ев': 157, 'ег': 158, 'ед': 159, 'ее': 160, 'еж': 161, 'ез': 162, 'еи': 163, 'ей': 164, 'ек': 165, 'ел': 166, 'ем': 167, 'ен': 168, 'ео': 169, 'еп': 170, 'ер': 171, 'ес': 172, 'ет': 173, 'еу': 174, 'еф': 175, 'ех': 176, 'ец': 177, 'еч': 178, 'еш': 179, 'ещ': 180, 'еь': 181, 'еы': 182, 'еэ': 183, 'ею': 184, 'ея': 185, 'жа': 186, 'жб': 187, 'жв': 188, 'жг': 189, 'жд': 190, 'же': 191, 'жж': 192, 'жз': 193, 'жи': 194, 'жй': 195, 'жк': 196, 'жл': 197, 'жм': 198, 'жн': 199, 'жо': 200, 'жп': 201, 'жр': 202, 'жс': 203, 'жт': 204, 'жу': 205, 'жф': 206, 'жх': 207, 'жц': 208, 'жч': 209, 'жш': 210, 'жщ': 211, 'жь': 212, 'жы': 213, 'жэ': 214, 'жю': 215, 'жя': 216, 'за': 217, 'зб': 218, 'зв': 219, 'зг': 220, 'зд': 221, 'зе': 222, 'зж': 223, 'зз': 224, 'зи': 225, 'зй': 226, 'зк': 227, 'зл': 228, 'зм': 229, 'зн': 230, 'зо': 231, 'зп': 232, 'зр': 233, 'зс': 234, 'зт': 235, 'зу': 236, 'зф': 237, 'зх': 238, 'зц': 239, 'зч': 240, 'зш': 241, 'зщ': 242, 'зь': 243, 'зы': 244, 'зэ': 245, 'зю': 246, 'зя': 247, 'иа': 248, 'иб': 249, 'ив': 250, 'иг': 251, 'ид': 252, 'ие': 253, 'иж': 254, 'из': 255, 'ии': 256, 'ий': 257, 'ик': 258, 'ил': 259, 'им': 260, 'ин': 261, 'ио': 262, 'ип': 263, 'ир': 264, 'ис': 265, 'ит': 266, 'иу': 267, 'иф': 268, 'их': 269, 'иц': 270, 'ич': 271, 'иш': 272, 'ищ': 273, 'иь': 274, 'иы': 275, 'иэ': 276, 'ию': 277, 'ия': 278, 'йа': 279, 'йб': 280, 'йв': 281, 'йг': 282, 'йд': 283, 'йе': 284, 'йж': 285, 'йз': 286, 'йи': 287, 'йй': 288, 'йк': 289, 'йл': 290, 'йм': 291, 'йн': 292, 'йо': 293, 'йп': 294, 'йр': 295, 'йс': 296, 'йт': 297, 'йу': 298, 'йф': 299, 'йх': 300, 'йц': 301, 'йч': 302, 'йш': 303, 'йщ': 304, 'йь': 305, 'йы': 306, 'йэ': 307, 'йю': 308, 'йя': 309, 'ка': 310, 'кб': 311, 'кв': 312, 'кг': 313, 'кд': 314, 'ке': 315, 'кж': 316, 'кз': 317, 'ки': 318, 'кй': 319, 'кк': 320, 'кл': 321, 'км': 322, 'кн': 323, 'ко': 324, 'кп': 325, 'кр': 326, 'кс': 327, 'кт': 328, 'ку': 329, 'кф': 330, 'кх': 331, 'кц': 332, 'кч': 333, 'кш': 334, 'кщ': 335, 'кь': 336, 'кы': 337, 'кэ': 338, 'кю': 339, 'кя': 340, 'ла': 341, 'лб': 342, 'лв': 343, 'лг': 344, 'лд': 345, 'ле': 346, 'лж': 347, 'лз': 348, 'ли': 349, 'лй': 350, 'лк': 351, 'лл': 352, 'лм': 353, 'лн': 354, 'ло': 355, 'лп': 356, 'лр': 357, 'лс': 358, 'лт': 359, 'лу': 360, 'лф': 361, 'лх': 362, 'лц': 363, 'лч': 364, 'лш': 365, 'лщ': 366, 'ль': 367, 'лы': 368, 'лэ': 369, 'лю': 370, 'ля': 371, 'ма': 372, 'мб': 373, 'мв': 374, 'мг': 375, 'мд': 376, 'ме': 377, 'мж': 378, 'мз': 379, 'ми': 380, 'мй': 381, 'мк': 382, 'мл': 383, 'мм': 384, 'мн': 385, 'мо': 386, 'мп': 387, 'мр': 388, 'мс': 389, 'мт': 390, 'му': 391, 'мф': 392, 'мх': 393, 'мц': 394, 'мч': 395, 'мш': 396, 'мщ': 397, 'мь': 398, 'мы': 399, 'мэ': 400, 'мю': 401, 'мя': 402, 'на': 403, 'нб': 404, 'нв': 405, 'нг': 406, 'нд': 407, 'не': 408, 'нж': 409, 'нз': 410, 'ни': 411, 'нй': 412, 'нк': 413, 'нл': 414, 'нм': 415, 'нн': 416, 'но': 417, 'нп': 418, 'нр': 419, 'нс': 420, 'нт': 421, 'ну': 422, 'нф': 423, 'нх': 424, 'нц': 425, 'нч': 426, 'нш': 427, 'нщ': 428, 'нь': 429, 'ны': 430, 'нэ': 431, 'ню': 432, 'ня': 433, 'оа': 434, 'об': 435, 'ов': 436, 'ог': 437, 'од': 438, 'ое': 439, 'ож': 440, 'оз': 441, 'ои': 442, 'ой': 443, 'ок': 444, 'ол': 445, 'ом': 446, 'он': 447, 'оо': 448, 'оп': 449, 'ор': 450, 'ос': 451, 'от': 452, 'оу': 453, 'оф': 454, 'ох': 455, 'оц': 456, 'оч': 457, 'ош': 458, 'ощ': 459, 'оь': 460, 'оы': 461, 'оэ': 462, 'ою': 463, 'оя': 464, 'па': 465, 'пб': 466, 'пв': 467, 'пг': 468, 'пд': 469, 'пе': 470, 'пж': 471, 'пз': 472, 'пи': 473, 'пй': 474, 'пк': 475, 'пл': 476, 'пм': 477, 'пн': 478, 'по': 479, 'пп': 480, 'пр': 481, 'пс': 482, 'пт': 483, 'пу': 484, 'пф': 485, 'пх': 486, 'пц': 487, 'пч': 488, 'пш': 489, 'пщ': 490, 'пь': 491, 'пы': 492, 'пэ': 493, 'пю': 494, 'пя': 495, 'ра': 496, 'рб': 497, 'рв': 498, 'рг': 499, 'рд': 500, 'ре': 501, 'рж': 502, 'рз': 503, 'ри': 504, 'рй': 505, 'рк': 506, 'рл': 507, 'рм': 508, 'рн': 509, 'ро': 510, 'рп': 511, 'рр': 512, 'рс': 513, 'рт': 514, 'ру': 515, 'рф': 516, 'рх': 517, 'рц': 518, 'рч': 519, 'рш': 520, 'рщ': 521, 'рь': 522, 'ры': 523, 'рэ': 524, 'рю': 525, 'ря': 526, 'са': 527, 'сб': 528, 'св': 529, 'сг': 530, 'сд': 531, 'се': 532, 'сж': 533, 'сз': 534, 'си': 535, 'сй': 536, 'ск': 537, 'сл': 538, 'см': 539, 'сн': 540, 'со': 541, 'сп': 542, 'ср': 543, 'сс': 544, 'ст': 545, 'су': 546, 'сф': 547, 'сх': 548, 'сц': 549, 'сч': 550, 'сш': 551, 'сщ': 552, 'сь': 553, 'сы': 554, 'сэ': 555, 'сю': 556, 'ся': 557, 'та': 558, 'тб': 559, 'тв': 560, 'тг': 561, 'тд': 562, 'те': 563, 'тж': 564, 'тз': 565, 'ти': 566, 'тй': 567, 'тк': 568, 'тл': 569, 'тм': 570, 'тн': 571, 'то': 572, 'тп': 573, 'тр': 574, 'тс': 575, 'тт': 576, 'ту': 577, 'тф': 578, 'тх': 579, 'тц': 580, 'тч': 581, 'тш': 582, 'тщ': 583, 'ть': 584, 'ты': 585, 'тэ': 586, 'тю': 587, 'тя': 588, 'уа': 589, 'уб': 590, 'ув': 591, 'уг': 592, 'уд': 593, 'уе': 594, 'уж': 595, 'уз': 596, 'уи': 597, 'уй': 598, 'ук': 599, 'ул': 600, 'ум': 601, 'ун': 602, 'уо': 603, 'уп': 604, 'ур': 605, 'ус': 606, 'ут': 607, 'уу': 608, 'уф': 609, 'ух': 610, 'уц': 611, 'уч': 612, 'уш': 613, 'ущ': 614, 'уь': 615, 'уы': 616, 'уэ': 617, 'ую': 618, 'уя': 619, 'фа': 620, 'фб': 621, 'фв': 622, 'фг': 623, 'фд': 624, 'фе': 625, 'фж': 626, 'фз': 627, 'фи': 628, 'фй': 629, 'фк': 630, 'фл': 631, 'фм': 632, 'фн': 633, 'фо': 634, 'фп': 635, 'фр': 636, 'фс': 637, 'фт': 638, 'фу': 639, 'фф': 640, 'фх': 641, 'фц': 642, 'фч': 643, 'фш': 644, 'фщ': 645, 'фь': 646, 'фы': 647, 'фэ': 648, 'фю': 649, 'фя': 650, 'ха': 651, 'хб': 652, 'хв': 653, 'хг': 654, 'хд': 655, 'хе': 656, 'хж': 657, 'хз': 658, 'хи': 659, 'хй': 660, 'хк': 661, 'хл': 662, 'хм': 663, 'хн': 664, 'хо': 665, 'хп': 666, 'хр': 667, 'хс': 668, 'хт': 669, 'ху': 670, 'хф': 671, 'хх': 672, 'хц': 673, 'хч': 674, 'хш': 675, 'хщ': 676, 'хь': 677, 'хы': 678, 'хэ': 679, 'хю': 680, 'хя': 681, 'ца': 682, 'цб': 683, 'цв': 684, 'цг': 685, 'цд': 686, 'це': 687, 'цж': 688, 'цз': 689, 'ци': 690, 'цй': 691, 'цк': 692, 'цл': 693, 'цм': 694, 'цн': 695, 'цо': 696, 'цп': 697, 'цр': 698, 'цс': 699, 'цт': 700, 'цу': 701, 'цф': 702, 'цх': 703, 'цц': 704, 'цч': 705, 'цш': 706, 'цщ': 707, 'ць': 708, 'цы': 709, 'цэ': 710, 'цю': 711, 'ця': 712, 'ча': 713, 'чб': 714, 'чв': 715, 'чг': 716, 'чд': 717, 'че': 718, 'чж': 719, 'чз': 720, 'чи': 721, 'чй': 722, 'чк': 723, 'чл': 724, 'чм': 725, 'чн': 726, 'чо': 727, 'чп': 728, 'чр': 729, 'чс': 730, 'чт': 731, 'чу': 732, 'чф': 733, 'чх': 734, 'чц': 735, 'чч': 736, 'чш': 737, 'чщ': 738, 'чь': 739, 'чы': 740, 'чэ': 741, 'чю': 742, 'чя': 743, 'ша': 744, 'шб': 745, 'шв': 746, 'шг': 747, 'шд': 748, 'ше': 749, 'шж': 750, 'шз': 751, 'ши': 752, 'шй': 753, 'шк': 754, 'шл': 755, 'шм': 756, 'шн': 757, 'шо': 758, 'шп': 759, 'шр': 760, 'шс': 761, 'шт': 762, 'шу': 763, 'шф': 764, 'шх': 765, 'шц': 766, 'шч': 767, 'шш': 768, 'шщ': 769, 'шь': 770, 'шы': 771, 'шэ': 772, 'шю': 773, 'шя': 774, 'ща': 775, 'щб': 776, 'щв': 777, 'щг': 778, 'щд': 779, 'ще': 780, 'щж': 781, 'щз': 782, 'щи': 783, 'щй': 784, 'щк': 785, 'щл': 786, 'щм': 787, 'щн': 788, 'що': 789, 'щп': 790, 'щр': 791, 'щс': 792, 'щт': 793, 'щу': 794, 'щф': 795, 'щх': 796, 'щц': 797, 'щч': 798, 'щш': 799, 'щщ': 800, 'щь': 801, 'щы': 802, 'щэ': 803, 'щю': 804, 'щя': 805, 'ьа': 806, 'ьб': 807, 'ьв': 808, 'ьг': 809, 'ьд': 810, 'ье': 811, 'ьж': 812, 'ьз': 813, 'ьи': 814, 'ьй': 815, 'ьк': 816, 'ьл': 817, 'ьм': 818, 'ьн': 819, 'ьо': 820, 'ьп': 821, 'ьр': 822, 'ьс': 823, 'ьт': 824, 'ьу': 825, 'ьф': 826, 'ьх': 827, 'ьц': 828, 'ьч': 829, 'ьш': 830, 'ьщ': 831, 'ьь': 832, 'ьы': 833, 'ьэ': 834, 'ью': 835, 'ья': 836, 'ыа': 837, 'ыб': 838, 'ыв': 839, 'ыг': 840, 'ыд': 841, 'ые': 842, 'ыж': 843, 'ыз': 844, 'ыи': 845, 'ый': 846, 'ык': 847, 'ыл': 848, 'ым': 849, 'ын': 850, 'ыо': 851, 'ып': 852, 'ыр': 853, 'ыс': 854, 'ыт': 855, 'ыу': 856, 'ыф': 857, 'ых': 858, 'ыц': 859, 'ыч': 860, 'ыш': 861, 'ыщ': 862, 'ыь': 863, 'ыы': 864, 'ыэ': 865, 'ыю': 866, 'ыя': 867, 'эа': 868, 'эб': 869, 'эв': 870, 'эг': 871, 'эд': 872, 'эе': 873, 'эж': 874, 'эз': 875, 'эи': 876, 'эй': 877, 'эк': 878, 'эл': 879, 'эм': 880, 'эн': 881, 'эо': 882, 'эп': 883, 'эр': 884, 'эс': 885, 'эт': 886, 'эу': 887, 'эф': 888, 'эх': 889, 'эц': 890, 'эч': 891, 'эш': 892, 'эщ': 893, 'эь': 894, 'эы': 895, 'ээ': 896, 'эю': 897, 'эя': 898, 'юа': 899, 'юб': 900, 'юв': 901, 'юг': 902, 'юд': 903, 'юе': 904, 'юж': 905, 'юз': 906, 'юи': 907, 'юй': 908, 'юк': 909, 'юл': 910, 'юм': 911, 'юн': 912, 'юо': 913, 'юп': 914, 'юр': 915, 'юс': 916, 'ют': 917, 'юу': 918, 'юф': 919, 'юх': 920, 'юц': 921, 'юч': 922, 'юш': 923, 'ющ': 924, 'юь': 925, 'юы': 926, 'юэ': 927, 'юю': 928, 'юя': 929, 'яа': 930, 'яб': 931, 'яв': 932, 'яг': 933, 'яд': 934, 'яе': 935, 'яж': 936, 'яз': 937, 'яи': 938, 'яй': 939, 'як': 940, 'ял': 941, 'ям': 942, 'ян': 943, 'яо': 944, 'яп': 945, 'яр': 946, 'яс': 947, 'ят': 948, 'яу': 949, 'яф': 950, 'ях': 951, 'яц': 952, 'яч': 953, 'яш': 954, 'ящ': 955, 'яь': 956, 'яы': 957, 'яэ': 958, 'яю': 959, 'яя': 960}
num_to_bigrams = {0: 'аа', 1: 'аб', 2: 'ав', 3: 'аг', 4: 'ад', 5: 'ае', 6: 'аж', 7: 'аз', 8: 'аи', 9: 'ай', 10: 'ак', 11: 'ал', 12: 'ам', 13: 'ан', 14: 'ао', 15: 'ап', 16: 'ар', 17: 'ас', 18: 'ат', 19: 'ау', 20: 'аф', 21: 'ах', 22: 'ац', 23: 'ач', 24: 'аш', 25: 'ащ', 26: 'аь', 27: 'аы', 28: 'аэ', 29: 'аю', 30: 'ая', 31: 'ба', 32: 'бб', 33: 'бв', 34: 'бг', 35: 'бд', 36: 'бе', 37: 'бж', 38: 'бз', 39: 'би', 40: 'бй', 41: 'бк', 42: 'бл', 43: 'бм', 44: 'бн', 45: 'бо', 46: 'бп', 47: 'бр', 48: 'бс', 49: 'бт', 50: 'бу', 51: 'бф', 52: 'бх', 53: 'бц', 54: 'бч', 55: 'бш', 56: 'бщ', 57: 'бь', 58: 'бы', 59: 'бэ', 60: 'бю', 61: 'бя', 62: 'ва', 63: 'вб', 64: 'вв', 65: 'вг', 66: 'вд', 67: 'ве', 68: 'вж', 69: 'вз', 70: 'ви', 71: 'вй', 72: 'вк', 73: 'вл', 74: 'вм', 75: 'вн', 76: 'во', 77: 'вп', 78: 'вр', 79: 'вс', 80: 'вт', 81: 'ву', 82: 'вф', 83: 'вх', 84: 'вц', 85: 'вч', 86: 'вш', 87: 'вщ', 88: 'вь', 89: 'вы', 90: 'вэ', 91: 'вю', 92: 'вя', 93: 'га', 94: 'гб', 95: 'гв', 96: 'гг', 97: 'гд', 98: 'ге', 99: 'гж', 100: 'гз', 101: 'ги', 102: 'гй', 103: 'гк', 104: 'гл', 105: 'гм', 106: 'гн', 107: 'го', 108: 'гп', 109: 'гр', 110: 'гс', 111: 'гт', 112: 'гу', 113: 'гф', 114: 'гх', 115: 'гц', 116: 'гч', 117: 'гш', 118: 'гщ', 119: 'гь', 120: 'гы', 121: 'гэ', 122: 'гю', 123: 'гя', 124: 'да', 125: 'дб', 126: 'дв', 127: 'дг', 128: 'дд', 129: 'де', 130: 'дж', 131: 'дз', 132: 'ди', 133: 'дй', 134: 'дк', 135: 'дл', 136: 'дм', 137: 'дн', 138: 'до', 139: 'дп', 140: 'др', 141: 'дс', 142: 'дт', 143: 'ду', 144: 'дф', 145: 'дх', 146: 'дц', 147: 'дч', 148: 'дш', 149: 'дщ', 150: 'дь', 151: 'ды', 152: 'дэ', 153: 'дю', 154: 'дя', 155: 'еа', 156: 'еб', 157: 'ев', 158: 'ег', 159: 'ед', 160: 'ее', 161: 'еж', 162: 'ез', 163: 'еи', 164: 'ей', 165: 'ек', 166: 'ел', 167: 'ем', 168: 'ен', 169: 'ео', 170: 'еп', 171: 'ер', 172: 'ес', 173: 'ет', 174: 'еу', 175: 'еф', 176: 'ех', 177: 'ец', 178: 'еч', 179: 'еш', 180: 'ещ', 181: 'еь', 182: 'еы', 183: 'еэ', 184: 'ею', 185: 'ея', 186: 'жа', 187: 'жб', 188: 'жв', 189: 'жг', 190: 'жд', 191: 'же', 192: 'жж', 193: 'жз', 194: 'жи', 195: 'жй', 196: 'жк', 197: 'жл', 198: 'жм', 199: 'жн', 200: 'жо', 201: 'жп', 202: 'жр', 203: 'жс', 204: 'жт', 205: 'жу', 206: 'жф', 207: 'жх', 208: 'жц', 209: 'жч', 210: 'жш', 211: 'жщ', 212: 'жь', 213: 'жы', 214: 'жэ', 215: 'жю', 216: 'жя', 217: 'за', 218: 'зб', 219: 'зв', 220: 'зг', 221: 'зд', 222: 'зе', 223: 'зж', 224: 'зз', 225: 'зи', 226: 'зй', 227: 'зк', 228: 'зл', 229: 'зм', 230: 'зн', 231: 'зо', 232: 'зп', 233: 'зр', 234: 'зс', 235: 'зт', 236: 'зу', 237: 'зф', 238: 'зх', 239: 'зц', 240: 'зч', 241: 'зш', 242: 'зщ', 243: 'зь', 244: 'зы', 245: 'зэ', 246: 'зю', 247: 'зя', 248: 'иа', 249: 'иб', 250: 'ив', 251: 'иг', 252: 'ид', 253: 'ие', 254: 'иж', 255: 'из', 256: 'ии', 257: 'ий', 258: 'ик', 259: 'ил', 260: 'им', 261: 'ин', 262: 'ио', 263: 'ип', 264: 'ир', 265: 'ис', 266: 'ит', 267: 'иу', 268: 'иф', 269: 'их', 270: 'иц', 271: 'ич', 272: 'иш', 273: 'ищ', 274: 'иь', 275: 'иы', 276: 'иэ', 277: 'ию', 278: 'ия', 279: 'йа', 280: 'йб', 281: 'йв', 282: 'йг', 283: 'йд', 284: 'йе', 285: 'йж', 286: 'йз', 287: 'йи', 288: 'йй', 289: 'йк', 290: 'йл', 291: 'йм', 292: 'йн', 293: 'йо', 294: 'йп', 295: 'йр', 296: 'йс', 297: 'йт', 298: 'йу', 299: 'йф', 300: 'йх', 301: 'йц', 302: 'йч', 303: 'йш', 304: 'йщ', 305: 'йь', 306: 'йы', 307: 'йэ', 308: 'йю', 309: 'йя', 310: 'ка', 311: 'кб', 312: 'кв', 313: 'кг', 314: 'кд', 315: 'ке', 316: 'кж', 317: 'кз', 318: 'ки', 319: 'кй', 320: 'кк', 321: 'кл', 322: 'км', 323: 'кн', 324: 'ко', 325: 'кп', 326: 'кр', 327: 'кс', 328: 'кт', 329: 'ку', 330: 'кф', 331: 'кх', 332: 'кц', 333: 'кч', 334: 'кш', 335: 'кщ', 336: 'кь', 337: 'кы', 338: 'кэ', 339: 'кю', 340: 'кя', 341: 'ла', 342: 'лб', 343: 'лв', 344: 'лг', 345: 'лд', 346: 'ле', 347: 'лж', 348: 'лз', 349: 'ли', 350: 'лй', 351: 'лк', 352: 'лл', 353: 'лм', 354: 'лн', 355: 'ло', 356: 'лп', 357: 'лр', 358: 'лс', 359: 'лт', 360: 'лу', 361: 'лф', 362: 'лх', 363: 'лц', 364: 'лч', 365: 'лш', 366: 'лщ', 367: 'ль', 368: 'лы', 369: 'лэ', 370: 'лю', 371: 'ля', 372: 'ма', 373: 'мб', 374: 'мв', 375: 'мг', 376: 'мд', 377: 'ме', 378: 'мж', 379: 'мз', 380: 'ми', 381: 'мй', 382: 'мк', 383: 'мл', 384: 'мм', 385: 'мн', 386: 'мо', 387: 'мп', 388: 'мр', 389: 'мс', 390: 'мт', 391: 'му', 392: 'мф', 393: 'мх', 394: 'мц', 395: 'мч', 396: 'мш', 397: 'мщ', 398: 'мь', 399: 'мы', 400: 'мэ', 401: 'мю', 402: 'мя', 403: 'на', 404: 'нб', 405: 'нв', 406: 'нг', 407: 'нд', 408: 'не', 409: 'нж', 410: 'нз', 411: 'ни', 412: 'нй', 413: 'нк', 414: 'нл', 415: 'нм', 416: 'нн', 417: 'но', 418: 'нп', 419: 'нр', 420: 'нс', 421: 'нт', 422: 'ну', 423: 'нф', 424: 'нх', 425: 'нц', 426: 'нч', 427: 'нш', 428: 'нщ', 429: 'нь', 430: 'ны', 431: 'нэ', 432: 'ню', 433: 'ня', 434: 'оа', 435: 'об', 436: 'ов', 437: 'ог', 438: 'од', 439: 'ое', 440: 'ож', 441: 'оз', 442: 'ои', 443: 'ой', 444: 'ок', 445: 'ол', 446: 'ом', 447: 'он', 448: 'оо', 449: 'оп', 450: 'ор', 451: 'ос', 452: 'от', 453: 'оу', 454: 'оф', 455: 'ох', 456: 'оц', 457: 'оч', 458: 'ош', 459: 'ощ', 460: 'оь', 461: 'оы', 462: 'оэ', 463: 'ою', 464: 'оя', 465: 'па', 466: 'пб', 467: 'пв', 468: 'пг', 469: 'пд', 470: 'пе', 471: 'пж', 472: 'пз', 473: 'пи', 474: 'пй', 475: 'пк', 476: 'пл', 477: 'пм', 478: 'пн', 479: 'по', 480: 'пп', 481: 'пр', 482: 'пс', 483: 'пт', 484: 'пу', 485: 'пф', 486: 'пх', 487: 'пц', 488: 'пч', 489: 'пш', 490: 'пщ', 491: 'пь', 492: 'пы', 493: 'пэ', 494: 'пю', 495: 'пя', 496: 'ра', 497: 'рб', 498: 'рв', 499: 'рг', 500: 'рд', 501: 'ре', 502: 'рж', 503: 'рз', 504: 'ри', 505: 'рй', 506: 'рк', 507: 'рл', 508: 'рм', 509: 'рн', 510: 'ро', 511: 'рп', 512: 'рр', 513: 'рс', 514: 'рт', 515: 'ру', 516: 'рф', 517: 'рх', 518: 'рц', 519: 'рч', 520: 'рш', 521: 'рщ', 522: 'рь', 523: 'ры', 524: 'рэ', 525: 'рю', 526: 'ря', 527: 'са', 528: 'сб', 529: 'св', 530: 'сг', 531: 'сд', 532: 'се', 533: 'сж', 534: 'сз', 535: 'си', 536: 'сй', 537: 'ск', 538: 'сл', 539: 'см', 540: 'сн', 541: 'со', 542: 'сп', 543: 'ср', 544: 'сс', 545: 'ст', 546: 'су', 547: 'сф', 548: 'сх', 549: 'сц', 550: 'сч', 551: 'сш', 552: 'сщ', 553: 'сь', 554: 'сы', 555: 'сэ', 556: 'сю', 557: 'ся', 558: 'та', 559: 'тб', 560: 'тв', 561: 'тг', 562: 'тд', 563: 'те', 564: 'тж', 565: 'тз', 566: 'ти', 567: 'тй', 568: 'тк', 569: 'тл', 570: 'тм', 571: 'тн', 572: 'то', 573: 'тп', 574: 'тр', 575: 'тс', 576: 'тт', 577: 'ту', 578: 'тф', 579: 'тх', 580: 'тц', 581: 'тч', 582: 'тш', 583: 'тщ', 584: 'ть', 585: 'ты', 586: 'тэ', 587: 'тю', 588: 'тя', 589: 'уа', 590: 'уб', 591: 'ув', 592: 'уг', 593: 'уд', 594: 'уе', 595: 'уж', 596: 'уз', 597: 'уи', 598: 'уй', 599: 'ук', 600: 'ул', 601: 'ум', 602: 'ун', 603: 'уо', 604: 'уп', 605: 'ур', 606: 'ус', 607: 'ут', 608: 'уу', 609: 'уф', 610: 'ух', 611: 'уц', 612: 'уч', 613: 'уш', 614: 'ущ', 615: 'уь', 616: 'уы', 617: 'уэ', 618: 'ую', 619: 'уя', 620: 'фа', 621: 'фб', 622: 'фв', 623: 'фг', 624: 'фд', 625: 'фе', 626: 'фж', 627: 'фз', 628: 'фи', 629: 'фй', 630: 'фк', 631: 'фл', 632: 'фм', 633: 'фн', 634: 'фо', 635: 'фп', 636: 'фр', 637: 'фс', 638: 'фт', 639: 'фу', 640: 'фф', 641: 'фх', 642: 'фц', 643: 'фч', 644: 'фш', 645: 'фщ', 646: 'фь', 647: 'фы', 648: 'фэ', 649: 'фю', 650: 'фя', 651: 'ха', 652: 'хб', 653: 'хв', 654: 'хг', 655: 'хд', 656: 'хе', 657: 'хж', 658: 'хз', 659: 'хи', 660: 'хй', 661: 'хк', 662: 'хл', 663: 'хм', 664: 'хн', 665: 'хо', 666: 'хп', 667: 'хр', 668: 'хс', 669: 'хт', 670: 'ху', 671: 'хф', 672: 'хх', 673: 'хц', 674: 'хч', 675: 'хш', 676: 'хщ', 677: 'хь', 678: 'хы', 679: 'хэ', 680: 'хю', 681: 'хя', 682: 'ца', 683: 'цб', 684: 'цв', 685: 'цг', 686: 'цд', 687: 'це', 688: 'цж', 689: 'цз', 690: 'ци', 691: 'цй', 692: 'цк', 693: 'цл', 694: 'цм', 695: 'цн', 696: 'цо', 697: 'цп', 698: 'цр', 699: 'цс', 700: 'цт', 701: 'цу', 702: 'цф', 703: 'цх', 704: 'цц', 705: 'цч', 706: 'цш', 707: 'цщ', 708: 'ць', 709: 'цы', 710: 'цэ', 711: 'цю', 712: 'ця', 713: 'ча', 714: 'чб', 715: 'чв', 716: 'чг', 717: 'чд', 718: 'че', 719: 'чж', 720: 'чз', 721: 'чи', 722: 'чй', 723: 'чк', 724: 'чл', 725: 'чм', 726: 'чн', 727: 'чо', 728: 'чп', 729: 'чр', 730: 'чс', 731: 'чт', 732: 'чу', 733: 'чф', 734: 'чх', 735: 'чц', 736: 'чч', 737: 'чш', 738: 'чщ', 739: 'чь', 740: 'чы', 741: 'чэ', 742: 'чю', 743: 'чя', 744: 'ша', 745: 'шб', 746: 'шв', 747: 'шг', 748: 'шд', 749: 'ше', 750: 'шж', 751: 'шз', 752: 'ши', 753: 'шй', 754: 'шк', 755: 'шл', 756: 'шм', 757: 'шн', 758: 'шо', 759: 'шп', 760: 'шр', 761: 'шс', 762: 'шт', 763: 'шу', 764: 'шф', 765: 'шх', 766: 'шц', 767: 'шч', 768: 'шш', 769: 'шщ', 770: 'шь', 771: 'шы', 772: 'шэ', 773: 'шю', 774: 'шя', 775: 'ща', 776: 'щб', 777: 'щв', 778: 'щг', 779: 'щд', 780: 'ще', 781: 'щж', 782: 'щз', 783: 'щи', 784: 'щй', 785: 'щк', 786: 'щл', 787: 'щм', 788: 'щн', 789: 'що', 790: 'щп', 791: 'щр', 792: 'щс', 793: 'щт', 794: 'щу', 795: 'щф', 796: 'щх', 797: 'щц', 798: 'щч', 799: 'щш', 800: 'щщ', 801: 'щь', 802: 'щы', 803: 'щэ', 804: 'щю', 805: 'щя', 806: 'ьа', 807: 'ьб', 808: 'ьв', 809: 'ьг', 810: 'ьд', 811: 'ье', 812: 'ьж', 813: 'ьз', 814: 'ьи', 815: 'ьй', 816: 'ьк', 817: 'ьл', 818: 'ьм', 819: 'ьн', 820: 'ьо', 821: 'ьп', 822: 'ьр', 823: 'ьс', 824: 'ьт', 825: 'ьу', 826: 'ьф', 827: 'ьх', 828: 'ьц', 829: 'ьч', 830: 'ьш', 831: 'ьщ', 832: 'ьь', 833: 'ьы', 834: 'ьэ', 835: 'ью', 836: 'ья', 837: 'ыа', 838: 'ыб', 839: 'ыв', 840: 'ыг', 841: 'ыд', 842: 'ые', 843: 'ыж', 844: 'ыз', 845: 'ыи', 846: 'ый', 847: 'ык', 848: 'ыл', 849: 'ым', 850: 'ын', 851: 'ыо', 852: 'ып', 853: 'ыр', 854: 'ыс', 855: 'ыт', 856: 'ыу', 857: 'ыф', 858: 'ых', 859: 'ыц', 860: 'ыч', 861: 'ыш', 862: 'ыщ', 863: 'ыь', 864: 'ыы', 865: 'ыэ', 866: 'ыю', 867: 'ыя', 868: 'эа', 869: 'эб', 870: 'эв', 871: 'эг', 872: 'эд', 873: 'эе', 874: 'эж', 875: 'эз', 876: 'эи', 877: 'эй', 878: 'эк', 879: 'эл', 880: 'эм', 881: 'эн', 882: 'эо', 883: 'эп', 884: 'эр', 885: 'эс', 886: 'эт', 887: 'эу', 888: 'эф', 889: 'эх', 890: 'эц', 891: 'эч', 892: 'эш', 893: 'эщ', 894: 'эь', 895: 'эы', 896: 'ээ', 897: 'эю', 898: 'эя', 899: 'юа', 900: 'юб', 901: 'юв', 902: 'юг', 903: 'юд', 904: 'юе', 905: 'юж', 906: 'юз', 907: 'юи', 908: 'юй', 909: 'юк', 910: 'юл', 911: 'юм', 912: 'юн', 913: 'юо', 914: 'юп', 915: 'юр', 916: 'юс', 917: 'ют', 918: 'юу', 919: 'юф', 920: 'юх', 921: 'юц', 922: 'юч', 923: 'юш', 924: 'ющ', 925: 'юь', 926: 'юы', 927: 'юэ', 928: 'юю', 929: 'юя', 930: 'яа', 931: 'яб', 932: 'яв', 933: 'яг', 934: 'яд', 935: 'яе', 936: 'яж', 937: 'яз', 938: 'яи', 939: 'яй', 940: 'як', 941: 'ял', 942: 'ям', 943: 'ян', 944: 'яо', 945: 'яп', 946: 'яр', 947: 'яс', 948: 'ят', 949: 'яу', 950: 'яф', 951: 'ях', 952: 'яц', 953: 'яч', 954: 'яш', 955: 'ящ', 956: 'яь', 957: 'яы', 958: 'яэ', 959: 'яю', 960: 'яя'}
letters = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')

def findModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def linear_congruence(a,b,n):
    if math.gcd(a,n) == 1:
        return (findModInverse(a, n) * b) % n
    if math.gcd(a,n) > 1:
        if b % math.gcd(a, n) != 0:
            return None
        else:
            a1 = int(a / math.gcd(a,n))
            b1 = int(b / math.gcd(a,n))
            n1 = int(n / math.gcd(a,n))
            x1 = linear_congruence(a1,b1,n1)
            solutions = [i for i in range(x1,n,n1)]
            if not isinstance(solutions, list):
                solutions = [solutions]
            return solutions

def Letter_counter(text):
    count = Counter(text)
    return count;


def bigramscounter(text):
    length2_without = len(text) - 1
    couples_2 = []

    for item in range(0, length2_without):
        couples_2.append(text[item:item + 2])
    a_2_without = Letter_counter(couples_2)
    a_2_without = dict(a_2_without)
    a_2_without_sort = sorted(a_2_without.items(), key=operator.itemgetter(1))
    return list(dict(a_2_without_sort).keys())[-5:]

def indexer(text):
    len_of_text = len(text)
    letters_map = {i:0 for i in letters}
    for letter in text:
        if letter in letters_map:
            letters_map[letter] += 1
        else:
            continue
    arr = sum([letters_map[item] * (letters_map[item] - 1) for item in letters_map])
    div = len_of_text * (len_of_text - 1)
    idex_text = arr / div
    return idex_text

def decodeafin(text,a,b):
    bob_text = ''
    for i in range(0, len(text), 2):
        y = bigrams_to_num[text[i]+text[i+1]]
        x = (findModInverse(a, 31 ** 2) * (y - b)) % (31 ** 2)
        x = num_to_bigrams[x]
        bob_text += x
    return bob_text


most_pop_bigrams = ["ст", "но", "то", "на", "ен"]
text = open('text.txt','r').read().replace('\n','')
print('варіант 6 шифртекст   ',text)
most_used_bigrams = bigramscounter(text)[::-1]
print('найчаастіші біграми шифртексту',most_used_bigrams)
combine_bigrams = []
#print(most_used_bigrams)
#test = decodeafin(text,441,310)
#bob_text = indexer(test)
#print(bob_text)

for m1 in most_pop_bigrams:
        for m2 in most_pop_bigrams:
            for bigr1 in most_used_bigrams:
                for bigr2 in most_used_bigrams:
                    if (m1 != m2 and bigr1 != bigr2):
                        combine_bigrams.append([m1,m2,bigr1,bigr2])



for X1,X2,Y1,Y2 in combine_bigrams:
    X1_X2 = bigrams_to_num[X1] - bigrams_to_num[X2]
    Y1_Y2 = bigrams_to_num[Y1] - bigrams_to_num[Y2]

    if X1_X2 < 0:
        X1_X2 += 31 ** 2
    if Y1_Y2 < 0:
        Y1_Y2 += 31 ** 2
    a_keys = linear_congruence(X1_X2, Y1_Y2, 31 ** 2)
    if not isinstance(a_keys, list):
        a_keys = [a_keys]
    if None not in a_keys:
            for a in a_keys:
                if math.gcd(a, 31 ** 2) != 1:
                    continue

                b = (bigrams_to_num[Y1] - a * bigrams_to_num[X1]) % 31 ** 2
                if b < 0:
                    b += 31 ** 2
                bob_text = decodeafin(text,a,b)
                idex_text = indexer(bob_text)
                if idex_text > 0.054:
                    print(idex_text)
                    key = [a,b]
                    print('ключ шифртексту',key)
                    print('розшифрований текст:  ',bob_text)