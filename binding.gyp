{
  "targets": [
    {
      "target_name": "ariaObjects",
      'type': 'static_library',
      "sources": [
        "src/ArActionAvoidFront.cpp",
        "src/ArActionAvoidSide.cpp",
        "src/ArActionBumpers.cpp",
        "src/ArActionColorFollow.cpp",
        "src/ArActionConstantVelocity.cpp",
        "src/ArAction.cpp",
        "src/ArActionDeceleratingLimiter.cpp",
        "src/ArActionDesired.cpp",
        "src/ArActionDriveDistance.cpp",
        "src/ArActionGoto.cpp",
        "src/ArActionGotoStraight.cpp",
        "src/ArActionGroup.cpp",
        "src/ArActionGroups.cpp",
        "src/ArActionInput.cpp",
        "src/ArActionIRs.cpp",
        "src/ArActionJoydrive.cpp",
        "src/ArActionKeydrive.cpp",
        "src/ArActionLimiterBackwards.cpp",
        "src/ArActionLimiterForwards.cpp",
        "src/ArActionLimiterRot.cpp",
        "src/ArActionLimiterTableSensor.cpp",
        "src/ArActionMovementParameters.cpp",
        "src/ArActionMovementParametersDebugging.cpp",
        "src/ArActionRatioInput.cpp",
        "src/ArActionRobotJoydrive.cpp",
        "src/ArActionStallRecover.cpp",
        "src/ArActionStop.cpp",
        "src/ArActionTriangleDriveTo.cpp",
        "src/ArActionTurn.cpp",
        "src/ArACTS.cpp",
        "src/ArAMPTU.cpp",
        "src/ArAnalogGyro.cpp",
        "src/ArArg.cpp",
        "src/ArArgumentBuilder.cpp",
        "src/ArArgumentParser.cpp",
        "src/ArASyncTask.cpp",
        "src/ArBasePacket.cpp",
        "src/ArBatteryConnector.cpp",
        "src/ArBatteryMTX.cpp",
        "src/ArBumpers.cpp",
        "src/ArCameraCollection.cpp",
        "src/ArCameraCommands.cpp",
        "src/ArCondition_LIN.cpp",
        "src/ArConfigArg.cpp",
        "src/ArConfig.cpp",
        "src/ArConfigGroup.cpp",
        "src/ArDataLogger.cpp",
        "src/ArDeviceConnection.cpp",
        "src/ArDPPTU.cpp",
        "src/ArFileParser.cpp",
        "src/ArForbiddenRangeDevice.cpp",
        "src/ArFunctorASyncTask.cpp",
        "src/ArGPSConnector.cpp",
        "src/ArGPSCoords.cpp",
        "src/ArGPS.cpp",
        "src/ArGripper.cpp",
        "src/Aria.cpp",
        "src/ariaUtil.cpp",
        "src/ArInterpolation.cpp",
        "src/ArIrrfDevice.cpp",
        "src/ArIRs.cpp",
        "src/ArJoyHandler.cpp",
        "src/ArJoyHandler_LIN.cpp",
        "src/ArKeyHandler.cpp",
        "src/ArLaserConnector.cpp",
        "src/ArLaser.cpp",
        "src/ArLaserFilter.cpp",
        "src/ArLaserLogger.cpp",
        "src/ArLaserReflectorDevice.cpp",
        "src/ArLCDConnector.cpp",
        "src/ArLCDMTX.cpp",
        "src/ArLineFinder.cpp",
        "src/ArLMS1XX.cpp",
        "src/ArLMS2xx.cpp",
        "src/ArLMS2xxPacket.cpp",
        "src/ArLMS2xxPacketReceiver.cpp",
        "src/ArLog.cpp",
        "src/ArLogFileConnection.cpp",
        "src/ArMapComponents.cpp",
        "src/ArMap.cpp",
        "src/ArMapInterface.cpp",
        "src/ArMapObject.cpp",
        "src/ArMapUtils.cpp",
        "src/ArMD5Calculator.cpp",
        "src/ArMode.cpp",
        "src/ArModes.cpp",
        "src/ArModule.cpp",
        "src/ArModuleLoader.cpp",
        "src/ArMTXIO.cpp",
        "src/ArMutex.cpp",
        "src/ArMutex_LIN.cpp",
        "src/ArNetServer.cpp",
        "src/ArNMEAParser.cpp",
        "src/ArNovatelGPS.cpp",
        "src/ArP2Arm.cpp",
        "src/ArPriorityResolver.cpp",
        "src/ArPTZConnector.cpp",
        "src/ArPTZ.cpp",
        "src/ArRangeBuffer.cpp",
        "src/ArRangeDevice.cpp",
        "src/ArRangeDeviceThreaded.cpp",
        "src/ArRatioInputJoydrive.cpp",
        "src/ArRatioInputKeydrive.cpp",
        "src/ArRatioInputRobotJoydrive.cpp",
        "src/ArRecurrentTask.cpp",
        "src/ArRobotBatteryPacketReader.cpp",
        "src/ArRobotConfig.cpp",
        "src/ArRobotConfigPacketReader.cpp",
        "src/ArRobotConnector.cpp",
        "src/ArRobot.cpp",
        "src/ArRobotJoyHandler.cpp",
        "src/ArRobotPacket.cpp",
        "src/ArRobotPacketReaderThread.cpp",
        "src/ArRobotPacketReceiver.cpp",
        "src/ArRobotPacketSender.cpp",
        "src/ArRobotParams.cpp",
        "src/ArRobotTypes.cpp",
        "src/ArRVisionPTZ.cpp",
        "src/ArS3Series.cpp",
        "src/ArSensorReading.cpp",
        "src/ArSerialConnection_LIN.cpp",
        "src/ArSick.cpp",
        "src/ArSignalHandler_LIN.cpp",
        "src/ArSimpleConnector.cpp",
        "src/ArSimulatedLaser.cpp",
        "src/ArSocket.cpp",
        "src/ArSocket_LIN.cpp",
        "src/ArSonarAutoDisabler.cpp",
        "src/ArSonarConnector.cpp",
        "src/ArSonarDevice.cpp",
        "src/ArSonarMTX.cpp",
        "src/ArSonyPTZ.cpp",
        "src/ArSoundPlayer.cpp",
        "src/ArSoundsQueue.cpp",
        "src/ArSpeech.cpp",
        "src/ArStringInfoGroup.cpp",
        "src/ArSyncLoop.cpp",
        "src/ArSyncTask.cpp",
        "src/ArSystemStatus.cpp",
        "src/ArSZSeries.cpp",
        "src/ArTCM2.cpp",
        "src/ArTCMCompassDirect.cpp",
        "src/ArTCMCompassRobot.cpp",
        "src/ArTcpConnection.cpp",
        "src/ArThread.cpp",
        "src/ArThread_LIN.cpp",
        "src/ArTransform.cpp",
        "src/ArTrimbleGPS.cpp",
        "src/ArUrg_2_0.cpp",
        "src/ArUrg.cpp",
        "src/ArVCC4.cpp",
        "src/ArVersalogicIO.cpp",
        "src/md5.cpp"
      ],
      "include_dirs": [
        "include"
      ],
      "libraries": [
        "-lpthread", "-lrt", "-ldl", "-lm"
      ],
      "cflags": [ "-Wall", "-D_REENTRANT"],
      "cflags!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ]
    },
    {
      "target_name": "AriaJS",
      "sources": [
        "javascript/AriaJS_wrap.cpp"
      ],
      "include_dirs": [
        "include"
      ],
      "libraries": [
        "-L../obj", "-lpthread", "-lrt", "-ldl"
      ],
      "dependencies": ["ariaObjects"],
      "cflags": [ "-Wall", "-D_REENTRANT"],
      "cflags!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ]
    },
    {
      "target_name": "sample",
      "sources": [
        "javascript/sample.cpp"
      ],
      "include_dirs": [
        "include"
      ],
      "libraries": [
        "-L../lib", "-lpthread", "-lrt", "-ldl", "-lAria"
      ],
      "cflags": [ "-Wall", "-D_REENTRANT"],
      "cflags!": [ "-fno-exceptions", "-fno-rtti" ],
      "cflags_cc!": [ "-fno-exceptions", "-fno-rtti" ]
    }
  ]
}