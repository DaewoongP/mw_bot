attrib				-R			.\Reference\Headers\*.*
xcopy				/y /s		.\Engine\Public\*.*					.\Reference\Headers\
attrib				+R			.\Reference\Headers\*.*

xcopy				/y /s		.\Engine\ThirdPartyLib\*.*			.\Reference\Librarys\

xcopy				/y			.\Engine\Bin\Engine.lib				.\Reference\Librarys\
xcopy				/y			.\Engine\Bin\Engine.idb				.\Reference\Librarys\
xcopy				/y			.\Engine\Bin\Engine.pdb				.\Reference\Librarys\

xcopy				/y			.\Engine\Bin\Engine_d.lib			.\Reference\Librarys\
xcopy				/y			.\Engine\Bin\Engine_d.idb			.\Reference\Librarys\
xcopy				/y			.\Engine\Bin\Engine_d.pdb			.\Reference\Librarys\

xcopy				/y			.\Engine\Bin\DPP_Debug\*.dll		.\Client\Bin\DPP_Debug\
xcopy				/y			.\Engine\Bin\DPP_Release\*.dll		.\Client\Bin\DPP_Release\
