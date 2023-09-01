"""Base package
"""
PACKAGE_NAME = 'PyFlowBase'
from collections import OrderedDict

from PyFlow.UI.UIInterfaces import IPackage

# Pins
from .Pins.AnyPin import AnyPin
from .Pins.BoolPin import BoolPin
from .Pins.ExecPin import ExecPin
from .Pins.FloatPin import FloatPin
from .Pins.IntPin import IntPin
from .Pins.StringPin import StringPin

# Function based nodes
from .FunctionLibraries.ArrayLib import ArrayLib
from .FunctionLibraries.BoolLib import BoolLib
from .FunctionLibraries.DefaultLib import DefaultLib
from .FunctionLibraries.FloatLib import FloatLib
from .FunctionLibraries.IntLib import IntLib
from .FunctionLibraries.MathLib import MathLib
from .FunctionLibraries.MathAbstractLib import MathAbstractLib
from .FunctionLibraries.RandomLib import RandomLib
from .FunctionLibraries.PathLib import PathLib

# Class based nodes
from .Nodes.branch import branch
from .Nodes.tick import tick
from .Nodes.charge import charge
from .Nodes.delay import delay
from .Nodes.deltaTime import deltaTime
from .Nodes.doN import doN
from .Nodes.doOnce import doOnce
from .Nodes.flipFlop import flipFlop
from .Nodes.forLoop import forLoop
from .Nodes.forLoopBegin import forLoopBegin
from .Nodes.loopEnd import loopEnd
from .Nodes.whileLoopBegin import whileLoopBegin
from .Nodes.forEachLoop import forEachLoop
from .Nodes.forLoopWithBreak import forLoopWithBreak
from .Nodes.retriggerableDelay import retriggerableDelay
from .Nodes.sequence import sequence
from .Nodes.switchOnString import switchOnString
from .Nodes.timer import timer
from .Nodes.whileLoop import whileLoop
from .Nodes.getVar import getVar
from .Nodes.setVar import setVar
from .Nodes.reroute import reroute
from .Nodes.rerouteExecs import rerouteExecs
from .Nodes.makeArray import makeArray
from .Nodes.makeList import makeList
from .Nodes.makeDict import makeDict
from .Nodes.makeAnyDict import makeAnyDict
from .Nodes.makeDictElement import makeDictElement
from .Nodes.dictKeys import dictKeys
from .Nodes.floatRamp import floatRamp
from .Nodes.colorRamp import colorRamp
from .Nodes.stringToArray import stringToArray
from .Nodes.cliexit import cliexit


from .Nodes.consoleOutput import consoleOutput
from .Nodes.address import address
from .Nodes.graphNodes import graphInputs, graphOutputs
from .Nodes.pythonNode import pythonNode
from .Nodes.compound import compound
from .Nodes.constant import constant
from .Nodes.convertTo import convertTo
from .Nodes.imageDisplay import imageDisplay


from .Nodes.commentNode import commentNode
from .Nodes.stickyNote import stickyNote

from .Tools.ScreenshotTool import ScreenshotTool
from .Tools.NodeBoxTool import NodeBoxTool
from .Tools.SearchResultsTool import SearchResultsTool
from .Tools.AlignLeftTool import AlignLeftTool
from .Tools.AlignRightTool import AlignRightTool
from .Tools.AlignTopTool import AlignTopTool
from .Tools.AlignBottomTool import AlignBottomTool
from .Tools.HistoryTool import HistoryTool
from .Tools.PropertiesTool import PropertiesTool
from .Tools.VariablesTool import VariablesTool
from .Tools.CompileTool import CompileTool
from .Tools.LoggerTool import LoggerTool

from .Exporters.PythonScriptExporter import PythonScriptExporter

# Factories
from .Factories.UIPinFactory import createUIPin
from .Factories.PinInputWidgetFactory import getInputWidget
from .Factories.UINodeFactory import createUINode

# Prefs widgets
from .PrefsWidgets.General import GeneralPreferences
from .PrefsWidgets.InputPrefs import InputPreferences
from .PrefsWidgets.ThemePrefs import ThemePreferences


_FOO_LIBS = {
    ArrayLib.__name__: ArrayLib(PACKAGE_NAME),
    BoolLib.__name__: BoolLib(PACKAGE_NAME),
    DefaultLib.__name__: DefaultLib(PACKAGE_NAME),
    FloatLib.__name__: FloatLib(PACKAGE_NAME),
    IntLib.__name__: IntLib(PACKAGE_NAME),
    MathLib.__name__: MathLib(PACKAGE_NAME),
    MathAbstractLib.__name__: MathAbstractLib(PACKAGE_NAME),
    RandomLib.__name__: RandomLib(PACKAGE_NAME),
    PathLib.__name__: PathLib(PACKAGE_NAME),
}


_NODES = {
    branch.__name__: branch,
    charge.__name__: charge,
    delay.__name__: delay,
    deltaTime.__name__: deltaTime,
    doN.__name__: doN,
    doOnce.__name__: doOnce,
    flipFlop.__name__: flipFlop,
    forLoop.__name__: forLoop,
    forLoopBegin.__name__: forLoopBegin,
    loopEnd.__name__: loopEnd,
    forLoopWithBreak.__name__: forLoopWithBreak,
    retriggerableDelay.__name__: retriggerableDelay,
    sequence.__name__: sequence,
    switchOnString.__name__: switchOnString,
    timer.__name__: timer,
    whileLoop.__name__: whileLoop,
    whileLoopBegin.__name__: whileLoopBegin,
    commentNode.__name__: commentNode,
    stickyNote.__name__: stickyNote,
    getVar.__name__: getVar,
    setVar.__name__: setVar,
    reroute.__name__: reroute,
    rerouteExecs.__name__: rerouteExecs,
    graphInputs.__name__: graphInputs,
    graphOutputs.__name__: graphOutputs,
    compound.__name__: compound,
    pythonNode.__name__: pythonNode,
    makeArray.__name__: makeArray,
    makeList.__name__: makeList,
    makeDict.__name__: makeDict,
    makeAnyDict.__name__: makeAnyDict,
    makeDictElement.__name__: makeDictElement,
    consoleOutput.__name__: consoleOutput,
    forEachLoop.__name__: forEachLoop,
    address.__name__: address,
    constant.__name__: constant,
    tick.__name__: tick,
    convertTo.__name__: convertTo,
    dictKeys.__name__: dictKeys,
    floatRamp.__name__: floatRamp,
    colorRamp.__name__: colorRamp,
    stringToArray.__name__: stringToArray,
    imageDisplay.__name__: imageDisplay,
    cliexit.__name__: cliexit
}

_PINS = {
    AnyPin.__name__: AnyPin,
    BoolPin.__name__: BoolPin,
    ExecPin.__name__: ExecPin,
    FloatPin.__name__: FloatPin,
    IntPin.__name__: IntPin,
    StringPin.__name__: StringPin,
}

# Toolbar will be created in following order
_TOOLS = OrderedDict()
_TOOLS[CompileTool.__name__] = CompileTool
_TOOLS[ScreenshotTool.__name__] = ScreenshotTool
_TOOLS[AlignLeftTool.__name__] = AlignLeftTool
_TOOLS[AlignRightTool.__name__] = AlignRightTool
_TOOLS[AlignTopTool.__name__] = AlignTopTool
_TOOLS[AlignBottomTool.__name__] = AlignBottomTool
_TOOLS[HistoryTool.__name__] = HistoryTool
_TOOLS[PropertiesTool.__name__] = PropertiesTool
_TOOLS[VariablesTool.__name__] = VariablesTool
_TOOLS[NodeBoxTool.__name__] = NodeBoxTool
_TOOLS[SearchResultsTool.__name__] = SearchResultsTool
_TOOLS[LoggerTool.__name__] = LoggerTool

_EXPORTERS = OrderedDict()
_EXPORTERS[PythonScriptExporter.__name__] = PythonScriptExporter


_PREFS_WIDGETS = OrderedDict()
_PREFS_WIDGETS["General"] = GeneralPreferences
_PREFS_WIDGETS["Input"] = InputPreferences
_PREFS_WIDGETS["Theme"] = ThemePreferences


class PyFlowBase(IPackage):
    """Base pyflow package
    """
    def __init__(self):
        super(PyFlowBase, self).__init__()

    @staticmethod
    def GetExporters():
        return _EXPORTERS

    @staticmethod
    def GetFunctionLibraries():
        return _FOO_LIBS

    @staticmethod
    def GetNodeClasses():
        return _NODES

    @staticmethod
    def GetPinClasses():
        return _PINS

    @staticmethod
    def GetToolClasses():
        return _TOOLS

    @staticmethod
    def UIPinsFactory():
        return createUIPin

    @staticmethod
    def UINodesFactory():
        return createUINode

    @staticmethod
    def PinsInputWidgetFactory():
        return getInputWidget

    @staticmethod
    def PrefsWidgets():
        return _PREFS_WIDGETS
