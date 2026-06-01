from pathlib import Path

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.classic.private_l1_cache_hierarchy import PrivateL1CacheHierarchy
from gem5.components.memory.single_channel import SingleChannelDDR3_1600
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.cpu_types import CPUTypes
from gem5.isas import ISA
from gem5.resources.resource import BinaryResource
from gem5.simulate.simulator import Simulator

binary_path = Path("low_power_riscv_iot/sensor_average").resolve()

cache_hierarchy = PrivateL1CacheHierarchy(
    l1d_size="16KiB",
    l1i_size="16KiB"
)

memory = SingleChannelDDR3_1600(size="512MiB")

processor = SimpleProcessor(
    cpu_type=CPUTypes.TIMING,
    isa=ISA.RISCV,
    num_cores=1
)

board = SimpleBoard(
    clk_freq="1500MHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy
)

board.set_se_binary_workload(BinaryResource(local_path=str(binary_path)))

simulator = Simulator(board=board)
simulator.run()

print("Simulation complete.")
