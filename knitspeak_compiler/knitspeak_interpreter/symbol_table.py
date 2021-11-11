"""Symbol Table structure holds definitions of stitches and context for number variables"""
from typing import Dict, Union

from knit_graphs.Knit_Graph import Pull_Direction
from knitspeak_compiler.knitspeak_interpreter.cable_definitions import Cable_Definition
from knitspeak_compiler.knitspeak_interpreter.stitch_definitions import Stitch_Definition, Stitch_Lean

class Symbol_Table:
    """
    A class used to keep track of how stitches and number variables have been defined. Includes language defaults
    """

    def __init__(self):
        self._symbol_table: Dict[str, Union[Cable_Definition, Stitch_Definition, int]] = {"k": self._knit(), "p": self._purl(),
                                                                                          "yo": self._yo(), "slip": self._slip()}
        self._decreases()
        self._cables()
        # set current row variable
        self._symbol_table["current_row"] = 0

    def _cables(self):
        # Add cable symbols keyed to their definitions to the symbol table
        #  (i.e., self._symbol_table[{cable_name}] = Cable_Definition(...))
        #  for every combination of right and left loop counts create cables that:
        #   lean left, lean right, lean left and purl, lean right and purl.
        for i in range(1, 4):
            for j in range(1, 4):
                for LP in ["", "p"]:
                    for RP in ["", "p"]:
                        for LEAN in ["l", "r"]:
                            symbol = "{}c{}{}|{}{}".format(LEAN, i, LP, j, RP)
                            self._symbol_table[symbol] = Cable_Definition(
                                left_crossing_loops=i,
                                right_crossing_loops=j,
                                left_crossing_pull_direction=Pull_Direction.BtF if LP == "" else Pull_Direction.FtB,
                                right_crossing_pull_direction=Pull_Direction.BtF if RP == "" else Pull_Direction.FtB,
                                cable_lean=Stitch_Lean.Left if LEAN == "l" else Stitch_Lean.Right)

    def _decreases(self):
        # Add decrease symbols keyed to their definitions to the symbol table
        #  (i.e., self._symbol_table[{stitch_name}] = Stitch_Definition(...)).
        # k2tog : knit two stitches together
        self._symbol_table["k2tog"] = Stitch_Definition(offset_to_parent_loops=[-1, 0])
        # k3tog : knit three stitches together
        self._symbol_table["k3tog"] = Stitch_Definition(offset_to_parent_loops=[-2, -1, 0])
        # p2tog : purl two stitches together
        self._symbol_table["p2tog"] = Stitch_Definition(pull_direction=Pull_Direction.FtB, offset_to_parent_loops=[-1, 0])
        # p3tog : purl three stitches together
        self._symbol_table["p3tog"] = Stitch_Definition(pull_direction=Pull_Direction.FtB, offset_to_parent_loops=[-2, -1, 0])
        # skpo : slip, knit, pass the slipped stitch over the knit stitch
        self._symbol_table["skpo"] = Stitch_Definition(offset_to_parent_loops=[0, 1])
        # sppo : slip, purl, pass the slipped stitch over the purl stitch
        self._symbol_table["sppo"] = Stitch_Definition(pull_direction=Pull_Direction.FtB, offset_to_parent_loops=[0, 1])
        # s2kpo : slip twice, knit, pass two slipped stitches over the knit stitch
        self._symbol_table["s2kpo"] = Stitch_Definition(offset_to_parent_loops=[0, 2, 1])
        # s2ppo : slip twice, purl, pass two slipped stitches over the knit stitch
        self._symbol_table["s2ppo"] = Stitch_Definition(pull_direction=Pull_Direction.FtB, offset_to_parent_loops=[0, 2, 1])
        # sk2po : slip, knit two together, pass the slipped stitch over k2tog
        self._symbol_table["sk2po"] = Stitch_Definition(offset_to_parent_loops=[-1, 0, 1])
        # sp2po : slip, purl two together, pass the slipped stitch over p2tog
        self._symbol_table["sp2po"] = Stitch_Definition(pull_direction=Pull_Direction.FtB, offset_to_parent_loops=[-1, 0, 1])

    @staticmethod
    def _slip() -> Stitch_Definition:
        # Return a Stitch Definition with no child_loops
        return Stitch_Definition(child_loops=0)

    @staticmethod
    def _yo() -> Stitch_Definition:
        # Return a Stitch Definition that will create a new loop with no parents
        return Stitch_Definition(offset_to_parent_loops=[])

    @staticmethod
    def _purl() -> Stitch_Definition:
        # Return a Stitch Definition that will purl the next available loop
        return Stitch_Definition(pull_direction=Pull_Direction.FtB)

    @staticmethod
    def _knit() -> Stitch_Definition:
        # Return a Stitch Definition that will knit the next available loop
        return Stitch_Definition()

    def __contains__(self, item: str):
        return item.lower() in self._symbol_table

    def __setitem__(self, key: str, value: Union[int, Stitch_Definition, Cable_Definition]):
        self._symbol_table[key.lower()] = value

    def __getitem__(self, item: str):
        return self._symbol_table[item.lower()]
