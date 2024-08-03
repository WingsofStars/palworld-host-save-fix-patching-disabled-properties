import subprocess
import fix_host_save as HostSaver

worldFolderName = ""
savePath = f'G:\\SteamLibrary\\steamapps\\common\\PalServer\\Pal\\Saved\\SaveGames\\0\\{worldFolderName}'
oldID = '00000000000000000000000000000001'
newID = '020B46CA000000000000000000000000'
GuildFix = "True"

command1 = subprocess.Popen(f'python palworld-save-tools-windows-v0.23.1\convert.py "{savePath}"\\Level.sav', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
output = command1.communicate(b'y\n')[0]
print(output)

command2 = subprocess.Popen(f'python palworld-save-tools-windows-v0.23.1\convert.py "{savePath}"\\Players\\{oldID}.sav', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
output = command2.communicate(b'y\n')[0]
print(output)

HostSaver.main(savePath, oldID, newID, GuildFix)
