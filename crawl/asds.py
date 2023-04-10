span_tag = ['13:42', '22:45', '10:22', '5:33', '2:32']
seq = 0
slen = len('13:42')
if slen >= 5:
    for tag in span_tag:
        value = tag
        # 10:00이 되면 길이가 5이므로 seq 1 증가시켜 다음 영상으로
        if (len(value) > 5):
            seq += 1
        elif (len(value) == 5):
            if(int(value[0:2]) > 15):
                seq += 1
        else:
            break
        
print(seq)