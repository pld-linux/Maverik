Summary:	A vr micro-Kernel
Name:		Maverik
Version:	5.1
Release:	1
Copyright:	GPL
Group:		Developments/Libraries
Vendor:		Advanced Interfaces Group
Source0:	ftp://aig.cs.man.ac.uk/pub/aig/Maverik/%{name}-%{version}.tar.gz
Source1:	ftp://aig.cs.man.ac.uk/pub/aig/Maverik/%{name}Demos-%{version}.tar.gz
Source2:	Maverik-5.1-1.rpm-extras.tgz
Patch:		Maverik-5.1-1-linux.patch
URL:		http://hegel.cs.man.ac.uk/systems/Maverik/
Buildroot:	/tmp/%{name}-%{version}-root

%description
GNU Maverik is a framework and library for developing VR applications (it is
not an end-user application). It provides optimised management of graphics
and peripheral driving capabilities for a single user. A novel feature of
GNU MAVERIK is its direct use of the applications own data structures. This
means significant performance benefits can be achieved through application
specific optmisations.

Under GNU/Linux, GNU MAVERIK can use 3DFx VOODOO cards in pairs to drive stereo
headsets. See the web pages (http://aig.cs.man.ac.uk) for more detail, and
examples of applications written using GNU MAVERIK.


%package demos
Summary:	Maverik Demos
Group:		Developments/libraries
Requires:	%{name} = %{version}

%description demos
Maverik demos. AIGLab, EscapeCity and LegibleCity.

%prep
%setup -q
%setup -q -T -D -b 1
%setup -q -T -D -a 2
%patch -p 1

%build
#export OS_TYPE="Linux"
#export MAV_HOME=`pwd`
#source setup_env
( ./setup --VRML97 --MESAPATH=/usr/X11R6 ; make ; make clean)

#export LD_LIBRARY_PATH=${LD_LIBRARY_PATH}:${RPM_BUILD_DIR}/Maverik-3.0b4/lib/Linux
#(cd examples; make)

# dont make examples they need incl and lib paths setting, and those
# are different between our build and the installed build. Fix that
# one day. For now a useful test for the user to try.
#(cd examples ; make ; make clean)

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version}
install -d $RPM_BUILD_ROOT/{%{_libdir},%{_includedir}/Maverik,%{_mandir}/man3}

install -s lib/*.so $RPM_BUILD_ROOT/%{_libdir}/
install incl/* $RPM_BUILD_ROOT/%{_includedir}/Maverik/

cp -a examples/* $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version}/
cp -a demos $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version}/

find $RPM_BUILD_ROOT/%{_prefix}/src/examples/%{name}-%{version} -type f \
	-exec strip --strip-unneeded {} \; || :

# manual
install doc/MFS/man3/* $RPM_BUILD_ROOT/%{_mandir}/man3/

rm -f %{_mandir}/man3/mav_{BBAlign,BBCompBB,BBCompInit,BBCompPt,BBDisplay, \
BBDisplayWithColour,BBDisplayWithSurfaceParams,BBGetCorner,BBIntersectsBB, \
BBIntersectsClipPlanes,BBIntersectsLine,HBBConstructFromSMS,HBBExecFn, \
HBBIntersect,HBBNew,HBBObjectNext,HBBObjectRmv,HBBPointerReset,HBBSize, \
SMSCallbackEmptyExec,SMSCallbackExecFnExec,SMSCallbackIntersectExec, \
SMSCallbackObjectAddExec,SMSCallbackObjectContainsExec,SMSCallbackObjectNextExec, \
SMSCallbackObjectNextSet,SMSCallbackObjectRmvExec,SMSCallbackPointerPopExec, \
SMSCallbackPointerPopSet,SMSCallbackPointerPushExec,SMSCallbackPointerPushSet, \
SMSCallbackPointerResetExec,SMSCallbackSizeExec,SMSDisplayUnCulled,SMSHBBNew, \
SMSModuleID,SMSModuleInit,SMSObjBB,SMSObjDraw,SMSObjDump,SMSObjGetMatrix, \
SMSObjGetUserdef,SMSObjID,SMSObjIntersect,TDMCursorBB,TDMCursorDraw, \
TDMCursorDump,TDMCursorGetSurfaceParams,TDMCursorGetUserdef,TDMCursorID, \
TDMModuleID,TDMModuleInit,TRModuleID,TRModuleInit,avatarBB,avatarDraw, \
avatarDump,avatarGetMatrix,avatarGetSurfaceParams,avatarGetUserdef,avatarID, \
avatarIntersect,avatarModuleID,avatarModuleInit,callbackBBExec,callbackBBSet, \
callbackCrossingExec,callbackCrossingSet,callbackDumpExec,callbackDumpSet, \
callbackExposeExec,callbackExposeSet,callbackGetMatrixExec,callbackGetMatrixSet, \
callbackGetSurfaceParamsExec,callbackGetSurfaceParamsSet,callbackGetUserdefExec, \
callbackGetUserdefSet,callbackIDExec,callbackIDSet,callbackIntersectExec, \
callbackIntersectSet,callbackKeyboardExec,callbackMapExec,callbackMapSet, \
callbackMouseExec,callbackResizeExec,callbackSysKeyboardExec,callbackSysMouseExec, \
clipPlanePrint,clipPlanesGetFromBB,clipPlanesGetFromPixels,clipPlanesPrint, \
compositeBB,compositeDraw,compositeDump,compositeGetMatrix,compositeGetSurfaceParams, \
compositeGetUserdef,compositeID,compositeIntersect,compositeReadAC3D, \
compositeReadAC3DBuf,compositeReadJIF,compositeReadVRML97,coneBB,coneDraw, \
coneDump,coneGetMatrix,coneGetSurfaceParams,coneGetUserdef,coneID,coneIntersect, \
ctorusBB,ctorusDraw,ctorusDump,ctorusGetMatrix,ctorusGetSurfaceParams, \
ctorusGetUserdef,ctorusID,ctorusIntersect,cylinderBB,cylinderDraw, \
cylinderDump,cylinderGetMatrix,cylinderGetSurfaceParams,cylinderGetUserdef, \
cylinderID,cylinderIntersect,deviceCalc,ellipseBB,ellipseDraw,ellipseDump, \
ellipseGetMatrix,ellipseGetSurfaceParams,ellipseGetUserdef,ellipseID, \
ellipseIntersect,exposeDefault,eyeMono,eyeRight,facetBB,facetDraw,facetDump, \
facetGetMatrix,facetGetSurfaceParams,facetGetUserdef,facetID,facetIntersect, \
frameFn0Rmv,frameFn1Add,frameFn1Rmv,frameFn2Add,frameFn2Rmv,frameFn3Add, \
frameFn3Rmv,frameFn4Add,frameFn4Rmv,free,gfx3DfxBoardSet,gfx3DfxModeSet, \
gfxAccumSet,gfxBackfaceCullGet,gfxBackfaceCullSet,gfxBackgroundColourSet, \
gfxBlendSet,gfxBufferReadSet,gfxClearA,gfxClearC,gfxClearCZ,gfxClearZ, \
gfxClipPlaneDisable,gfxClipPlaneEnable,gfxClipPlanesSet,gfxColourSet, \
gfxColourUse,gfxColouringModeUse,gfxDepthMaskSet,gfxDepthTestSet,gfxLightPos, \
gfxLightSet,gfxLightUse,gfxLightingModelSet,gfxLightingModelUse,gfxLineBegin, \
gfxLineClosedBegin,gfxLineClosedEnd,gfxLineEnd,gfxLineStippleSet,gfxLineWidthGet, \
gfxLineWidthSet,gfxListEnd,gfxListExec,gfxListNew,gfxListsDelete,gfxListsExec, \
gfxListsNew,gfxMaterialSet,gfxMaterialUse,gfxMatrixGet,gfxMatrixLoad, \
gfxMatrixMode,gfxMatrixMult,gfxMatrixPop,gfxMatrixPush,gfxMatrixScale, \
gfxMatrixTranslate,gfxMeshTBegin,gfxMeshTEnd,gfxModuleID,gfxModuleInit, \
gfxMultiSampleSet,gfxNormal,gfxNormalizeSet,gfxPerspectiveSet,gfxPixelDraw, \
gfxPixelRead,gfxPixelReadUByte,gfxPolygonBegin,gfxPolygonEnd,gfxPolygonModeSet, \
gfxRasterPos2DSet,gfxRasterPosSet,gfxStripQBegin,gfxStripQEnd,gfxStripTBegin, \
gfxStripTEnd,gfxTexCoord,gfxTextureEnv1Set,gfxTextureEnv2Set,gfxTextureSet, \
gfxTextureUse,gfxTrianglesBegin,gfxTrianglesEnd,gfxVertex,gfxViewPortSet, \
gfxVisualInfoGet,hellipseBB,hellipseDraw,hellipseDump,hellipseGetMatrix, \
hellipseGetSurfaceParams,hellipseGetUserdef,hellipseID,hellipseIntersect, \
hsphereBB,hsphereDraw,hsphereDump,hsphereGetMatrix,hsphereGetSurfaceParams, \
hsphereGetUserdef,hsphereID,hsphereIntersect,lineAxisPlaneIntersection, \
lineInfPlaneIntersection,linePrint,listDelete,listEmpty,listItemAdd, \
listItemContains,listItemNext,listItemRmv,listOrderedNew,listPointerPop, \
listPointerPush,listPointerReset,listPrint,listSize,mapDefault,matrixPrint, \
matrixStackGet,matrixStackPop,matrixYAxisGet,matrixYAxisSet,matrixZAxisGet, \
matrixZAxisSet,navigateForwards,navigateForwardsFixedUp,navigatePitch, \
navigatePitchFixedUp,navigateRight,navigateRightFixedUp,navigateRoll, \
navigateRotRight,navigateRotUp,navigateTransX,navigateTransY,navigateTransZ, \
navigateUp,navigateUpFixedUp,navigateYaw,navigateYawFixedUp,navigationModuleID, \
navigationModuleInit,objListDelete,objListEmpty,objListExecFn,objListIntersect, \
objListObjectNext,objListObjectRmv,objListPointerPop,objListPointerPush, \
objListPointerReset,objListSize,objectIntersectionPrint,objectIsTextured, \
objectIsTransparent,objectsModuleID,objectsModuleInit,paletteFontIndexEmptyGet, \
paletteFontIndexMatchGet,paletteLightIndexEmptyGet,paletteLightIndexMatchGet, \
paletteMaterialIndexEmptyGet,paletteMaterialIndexMatchGet,paletteTextureIndexEmptyGet, \
paletteTextureIndexMatchGet,polygonBB,polygonDraw,polygonDump,polygonGetMatrix, \
polygonGetSurfaceParams,polygonGetUserdef,polygonGrpBB,polygonGrpDraw, \
polygonGrpDump,polygonGrpGetMatrix,polygonGrpGetSurfaceParams,polygonGrpGetUserdef, \
polygonGrpID,polygonGrpIntersect,polygonID,polygonIntersect,polylineBB, \
polylineDraw,polylineDump,polylineGetMatrix,polylineGetSurfaceParams, \
polylineGetUserdef,polylineID,pyramidBB,pyramidDraw,pyramidDump, \
pyramidGetMatrix,pyramidGetSurfaceParams,pyramidGetUserdef,pyramidID, \
pyramidIntersect,quaternionPrint,randomSeed,rectangleBB,rectangleDraw, \
rectangleDump,rectangleGetMatrix,rectangleGetSurfaceParams,rectangleGetUserdef, \
rectangleID,rectangleIntersect,resizeDefault,rtorusBB,rtorusDraw,rtorusDump, \
rtorusGetMatrix,rtorusGetSurfaceParams,rtorusGetUserdef,rtorusID,rtorusIntersect, \
sphereBB,sphereDraw,sphereDump,sphereGetMatrix,sphereGetSurfaceParams, \
sphereGetUserdef,sphereID,sphereIntersect,stringDisplayCentre,stringDisplayLeft, \
stringDisplayRight,surfaceParamsPrint,teapotBB,teapotDraw,teapotDump, \
teapotGetMatrix,teapotGetSurfaceParams,teapotGetUserdef,teapotID,texCoordPrint, \
textBB,textDraw,textDump,textGetMatrix,textGetSurfaceParams,textGetUserdef, \
textID,texturedObjectsManage,timeGet,timePrint,timerPrint,timerStop, \
transparentObjectsManage,vectorCrossProduct,vectorDotProduct,vectorMag, \
vectorMult,vectorMult3x3,vectorMult4x4,vectorNormalize,vectorPrint, \
vectorRotate,vectorScalar,vectorSet,vectorSub,viewParamsPrint, \
windowsModuleID,windowsModuleInit}.3

echo ".so mav_BBCull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBDisplay.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBAlign.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBCompBB.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBCompPt.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_linePrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_timePrint.3
echo ".so mav_HBBObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBExecFn.3
echo ".so mav_HBBObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBSize.3
echo ".so mav_SMSObjListNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSHBBNew.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSObjBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_teapotBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_textBB.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_textDraw.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_textDump.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSObjID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_teapotID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_textID.3
echo ".so mav_eyeLeft.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_eyeMono.3
echo ".so mav_eyeLeft.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_eyeRight.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxClearA.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxClearC.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxClearZ.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxNormal.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxVertex.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listEmpty.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listSize.3
echo ".so mav_malloc.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_free.3
echo ".so mav_objListNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBNew.3
echo ".so mav_timerStart.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_timeGet.3
echo ".so mav_timerStart.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_timerStop.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorMag.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorSet.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorSub.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBCompInit.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBGetCorner.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBIntersectsBB.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBIntersectsLine.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_clipPlanePrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_clipPlanesPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_matrixPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_quaternionPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_texCoordPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_timerPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_viewParamsPrint.3
echo ".so mav_HBBObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBIntersect.3
echo ".so mav_HBBObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBObjectNext.3
echo ".so mav_HBBObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBObjectRmv.3
echo ".so mav_HBBObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBPointerReset.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMCursorBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polylineBB.3
echo ".so mav_boxBB.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleBB.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSObjDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMCursorDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polylineDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereDraw.3
echo ".so mav_boxDraw.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_teapotDraw.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSObjDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMCursorDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polylineDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereDump.3
echo ".so mav_boxDump.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_teapotDump.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSObjGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polylineGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_teapotGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_textGetMatrix.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSObjGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_teapotGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_textGetUserdef.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMCursorID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polylineID.3
echo ".so mav_boxID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleID.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSObjIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereIntersect.3
echo ".so mav_callbackDrawExec.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackBBExec.3
echo ".so mav_callbackDrawExec.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackDumpExec.3
echo ".so mav_callbackDrawExec.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackIDExec.3
echo ".so mav_callbackDrawSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackBBSet.3
echo ".so mav_callbackDrawSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackDumpSet.3
echo ".so mav_callbackDrawSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackIDSet.3
echo ".so mav_callbackMouseSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackMouseExec.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackExposeSet.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackMapExec.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackMapSet.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_exposeDefault.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_mapDefault.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_resizeDefault.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSModuleID.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMModuleID.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TRModuleID.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarModuleID.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxModuleID.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objectsModuleID.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_windowsModuleID.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSModuleInit.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMModuleInit.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TRModuleInit.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarModuleInit.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxModuleInit.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objectsModuleInit.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_windowsModuleInit.3
echo ".so mav_compositeRead.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeReadAC3D.3
echo ".so mav_compositeRead.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeReadJIF.3
echo ".so mav_devicePoll.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_deviceCalc.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn0Rmv.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn1Add.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn1Rmv.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn2Add.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn2Rmv.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn3Add.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn3Rmv.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn4Add.3
echo ".so mav_frameFn0Add.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_frameFn4Rmv.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfx3DfxBoardSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfx3DfxModeSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxAccumSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxBlendSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxBufferReadSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxClearCZ.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxClipPlanesSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxColourSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxColourUse.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxDepthMaskSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxDepthTestSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLightPos.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLightSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLightUse.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLineBegin.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLineClosedEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLineEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLineStippleSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLineWidthGet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLineWidthSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxListEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxListExec.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxListNew.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxListsDelete.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxListsExec.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxListsNew.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMaterialSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMaterialUse.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixGet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixLoad.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixMode.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixMult.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixPop.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixPush.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixScale.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMeshTBegin.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMeshTEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMultiSampleSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxNormalizeSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxPerspectiveSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxPixelDraw.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxPixelRead.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxPixelReadUByte.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxPolygonBegin.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxPolygonEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxPolygonModeSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxRasterPos2DSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxRasterPosSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxStripQBegin.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxStripQEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxStripTBegin.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxStripTEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxTexCoord.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxTextureEnv1Set.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxTextureEnv2Set.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxTextureSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxTextureUse.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxTrianglesBegin.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxTrianglesEnd.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxViewPortSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxVisualInfoGet.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listDelete.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listItemAdd.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listItemContains.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listItemNext.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listItemRmv.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listOrderedNew.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listPointerPop.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listPointerPush.3
echo ".so mav_listNew.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_listPointerReset.3
echo ".so mav_matrixStackPush.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_matrixStackGet.3
echo ".so mav_matrixStackPush.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_matrixStackPop.3
echo ".so mav_matrixXAxisGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_matrixYAxisGet.3
echo ".so mav_matrixXAxisGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_matrixZAxisGet.3
echo ".so mav_matrixXAxisSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_matrixYAxisSet.3
echo ".so mav_matrixXAxisSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_matrixZAxisSet.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateForwards.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigatePitch.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateRight.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateRoll.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateRotRight.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateRotUp.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateTransX.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateTransY.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateTransZ.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateUp.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateUpFixedUp.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateYaw.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListDelete.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListEmpty.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListExecFn.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListIntersect.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListObjectNext.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListObjectRmv.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListPointerPop.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListSize.3
echo ".so mav_random.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_randomSeed.3
echo ".so mav_stringDisplay.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_stringDisplayLeft.3
echo ".so mav_texturedObjectsRender.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objectIsTextured.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorDotProduct.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorMult.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorMult3x3.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorMult4x4.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorNormalize.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorRotate.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorScalar.3
echo ".so mav_BBCull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBDisplayWithColour.3
echo ".so mav_BBCullToClipPlanes.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBIntersectsClipPlanes.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objectIntersectionPrint.3
echo ".so mav_BBPrint.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_surfaceParamsPrint.3
echo ".so mav_HBBObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_HBBConstructFromSMS.3
echo ".so mav_SMSCallbackEmptySet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackEmptyExec.3
echo ".so mav_SMSCallbackExecFnSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackExecFnExec.3
echo ".so mav_SMSCallbackIntersectSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackIntersectExec.3
echo ".so mav_SMSCallbackObjectAddSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackObjectAddExec.3
echo ".so mav_SMSCallbackObjectRmvSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackObjectRmvExec.3
echo ".so mav_SMSCallbackPointerResetSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackObjectNextExec.3
echo ".so mav_SMSCallbackPointerResetSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackObjectNextSet.3
echo ".so mav_SMSCallbackPointerResetSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackPointerPopExec.3
echo ".so mav_SMSCallbackPointerResetSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackPointerPopSet.3
echo ".so mav_SMSCallbackPointerResetSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackPointerPushSet.3
echo ".so mav_SMSCallbackSizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackSizeExec.3
echo ".so mav_SMSDisplay.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSDisplayUnCulled.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpGetMatrix.3
echo ".so mav_boxGetMatrix.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleGetMatrix.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMCursorGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_avatarGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_coneGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ctorusGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_ellipseGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_facetGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hsphereGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polylineGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_pyramidGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rtorusGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_sphereGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_teapotGetSurfaceParams.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_textGetSurfaceParams.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_TDMCursorGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_cylinderGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_hellipseGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polylineGetUserdef.3
echo ".so mav_boxGetUserdef.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleGetUserdef.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpIntersect.3
echo ".so mav_boxIntersect.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_rectangleIntersect.3
echo ".so mav_callbackDrawExec.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackGetMatrixExec.3
echo ".so mav_callbackDrawExec.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackGetUserdefExec.3
echo ".so mav_callbackDrawExec.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackIntersectExec.3
echo ".so mav_callbackDrawSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackGetMatrixSet.3
echo ".so mav_callbackDrawSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackGetUserdefSet.3
echo ".so mav_callbackDrawSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackIntersectSet.3
echo ".so mav_callbackKeyboardSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackKeyboardExec.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackCrossingExec.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackCrossingSet.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackExposeExec.3
echo ".so mav_callbackResizeSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackResizeExec.3
echo ".so mav_callbackSysKeyboardSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackSysKeyboardExec.3
echo ".so mav_callbackSysMouseSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackSysMouseExec.3
echo ".so mav_callbacksModuleID.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigationModuleID.3
echo ".so mav_callbacksModuleInit.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigationModuleInit.3
echo ".so mav_clipPlanesGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_clipPlanesGetFromBB.3
echo ".so mav_clipPlanesGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_clipPlanesGetFromPixels.3
echo ".so mav_compositeRead.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeReadAC3DBuf.3
echo ".so mav_compositeRead.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_compositeReadVRML97.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxBackfaceCullGet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxBackfaceCullSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxBackgroundColourSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxClipPlaneDisable.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxClipPlaneEnable.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxColouringModeUse.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLightingModelSet.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLightingModelUse.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxLineClosedBegin.3
echo ".so mav_gfx.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_gfxMatrixTranslate.3
echo ".so mav_linePolygonIntersection.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_lineAxisPlaneIntersection.3
echo ".so mav_linePolygonIntersection.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_lineInfPlaneIntersection.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateForwardsFixedUp.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigatePitchFixedUp.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateRightFixedUp.3
echo ".so mav_navigateNull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_navigateYawFixedUp.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListPointerPush.3
echo ".so mav_objListObjectAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objListPointerReset.3
echo ".so mav_paletteColourIndexEmptyGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteFontIndexEmptyGet.3
echo ".so mav_paletteColourIndexEmptyGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteLightIndexEmptyGet.3
echo ".so mav_paletteColourIndexMatchGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteFontIndexMatchGet.3
echo ".so mav_paletteColourIndexMatchGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteLightIndexMatchGet.3
echo ".so mav_stringDisplay.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_stringDisplayCentre.3
echo ".so mav_stringDisplay.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_stringDisplayRight.3
echo ".so mav_texturedObjectsRender.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_texturedObjectsManage.3
echo ".so mav_transparentObjectsRender.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_objectIsTransparent.3
echo ".so mav_transparentObjectsRender.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_transparentObjectsManage.3
echo ".so mav_vectorAdd.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_vectorCrossProduct.3
echo ".so mav_BBCull.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_BBDisplayWithSurfaceParams.3
echo ".so mav_SMSCallbackObjectContainsSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackObjectContainsExec.3
echo ".so mav_SMSCallbackPointerResetSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackPointerPushExec.3
echo ".so mav_SMSCallbackPointerResetSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_SMSCallbackPointerResetExec.3
echo ".so mav_boxGetSurfaceParams.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_polygonGrpGetSurfaceParams.3
echo ".so mav_callbackDrawExec.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackGetSurfaceParamsExec.3
echo ".so mav_callbackDrawSet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_callbackGetSurfaceParamsSet.3
echo ".so mav_paletteColourIndexEmptyGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteMaterialIndexEmptyGet.3
echo ".so mav_paletteColourIndexEmptyGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteTextureIndexEmptyGet.3
echo ".so mav_paletteColourIndexMatchGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteMaterialIndexMatchGet.3
echo ".so mav_paletteColourIndexMatchGet.3" > $RPM_BUILD_ROOT/%{_mandir}/man3/mav_paletteTextureIndexMatchGet.3

gzip -9nf $RPM_BUILD_ROOT/%{_mandir}/man3/* README.rpm README FAQ VERSIONS \
	doc/MPG/ps/mpg.ps doc/MFS/ps/mfs.ps

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,755)
%doc {README.rpm,README,FAQ,VERSIONS}.gz
%doc doc/MPG/ps/mpg.ps.gz doc/MFS/ps/mfs.ps.gz doc/MFS/html
%attr(755, root, root) %{_libdir}/*.so
%dir %{_includedir}/Maverik
%attr(644, root, root) %{_includedir}/Maverik/*
%attr(644, root, root) %{_mandir}/man3/*
%dir %{_prefix}/src/examples/%{name}-%{version}
%{_prefix}/src/examples/%{name}-%{version}/MPG
%{_prefix}/src/examples/%{name}-%{version}/kernel
%{_prefix}/src/examples/%{name}-%{version}/misc
%{_prefix}/src/examples/%{name}-%{version}/Makefile
%{_prefix}/src/examples/%{name}-%{version}/README

%files demos
%defattr(-,root,root,755)
%{_prefix}/src/examples/%{name}-%{version}/demos

%changelog
* Thu Jul 08 1999 Jan Rêkorajski <baggins@pld.org.pl>
- FHS 2.0
- buildroot
- attr macros
- massive cleanup
