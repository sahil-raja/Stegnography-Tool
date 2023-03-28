import mainpage
import textSteg
import textInImageEncode
import textInImageDecode
import textInAudioEncode
import textInAudioDecode

if __name__ == '__main__':
    while(1):
        temp = mainpage.vp_start_gui()
        if temp == "Text In Text (Encode/Decode)":
            if textSteg.vp_start_gui() != "back":
                break

        elif temp == "Text In Image (Encode)":
            if textInImageEncode.vp_start_gui() != "back":
                break

        elif temp == "Text In Image (Decode)":
            if textInImageDecode.vp_start_gui() != "back":
                break
        
        elif temp == "Text / Audio / Image in Audio (Encode)":
            if textInAudioEncode.vp_start_gui() != "back":
                break
            
        elif temp == "Text / Audio / Image in Audio (Decode)":
            if textInAudioDecode.vp_start_gui() != "back":
                break
        else:
            break
