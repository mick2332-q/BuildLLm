def calculadora_ip(ip,mask):
    def transformar_ip_binario(ip):
        return '.'.join(f'{int(octeto):08b}' for octeto in ip.split('.'))
    def transformar_mask_binario(mask):
        mask_binario = '1' * int(mask) + '0' * (32 - int(mask))
        print(mask_binario)
        for i in range(0, 33, 8):
            mask_binario='.'.join(mask_binario[i:i+8])
            print(mask_binario)
    return transformar_ip_binario(ip), transformar_mask_binario(mask)

print(calculadora_ip('10.10.10.10', 8))



