import color_constants as cc

#print(cc.MAGENTA)

for color in cc.colors:
    print('<tr><td>' +
          color + '</td><td>' + cc.colors[color].hex_format() +
          '</td><td>' + 'RGB({},{},{})'.format(cc.colors[color].red,
                                  cc.colors[color].green,
                                  cc.colors[color].blue) + '</td>' +
          '<td style="background-color:' +
          cc.colors[color].hex_format() + '">&nbsp;</td></tr>')