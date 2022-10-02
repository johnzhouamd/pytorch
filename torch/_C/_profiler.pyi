from enum import Enum
from typing import List, Optional, Union

# defined in torch/csrc/profiler/python/init.cpp

class RecordScope(Enum):
    FUNCTION = ...
    BACKWARD_FUNCTION = ...
    TORCHSCRIPT_FUNCTION = ...
    KERNEL_FUNCTION_DTYPE = ...
    CUSTOM_CLASS = ...
    BUILD_FEATURE = ...
    LITE_INTERPRETER = ...
    USER_SCOPE = ...
    STATIC_RUNTIME_OP = ...
    STATIC_RUNTIME_MODEL = ...

class ProfilerState(Enum):
    Disable = ...
    CPU = ...
    CUDA = ...
    NVTX = ...
    ITT = ...
    KINETO = ...
    KINETO_GPU_FALLBACK = ...

class ActiveProfilerType: ...

class ProfilerActivity(Enum):
    CPU = ...
    CUDA = ...

class _ExperimentalConfig:
    def __init__(
        self,
        profiler_metrics: List[str] = ...,
        profiler_measure_per_kernel: bool = ...,
        verbose: bool = ...,
    ) -> None: ...
    ...

class ProfilerConfig:
    def __init__(
        self,
        state: ProfilerState,
        report_input_shapes: bool,
        profile_memory: bool,
        with_stack: bool,
        with_flops: bool,
        with_modules: bool,
        experimental_config: _ExperimentalConfig,
    ) -> None: ...
    ...

class _ProfilerEvent:
    tag: _EventType
    id: int
    correlation_id: int
    start_tid: int
    start_time_ns: int
    end_time_ns: int
    duration_time_ns: int
    parent: _ProfilerEvent
    children: List[_ProfilerEvent]
    extra_fields: Union[
        _ExtraFields_TorchOp,
        _ExtraFields_Backend,
        _ExtraFields_Allocation,
        _ExtraFields_OutOfMemory,
        _ExtraFields_PyCall,
        _ExtraFields_PyCCall,
        _ExtraFields_Kineto,
    ]
    def name(self) -> str: ...
    ...

class _PyFrameState:
    line_number: int
    function_name: str
    file_name: str
    ...

class _EventType(Enum):
    Allocation = ...
    Backend = ...
    PyCall = ...
    PyCCall = ...
    TorchOp = ...
    Kineto = ...

class _Inputs:
    shapes: List[List[int]]
    dtypes: List[str]
    tensor_metadata: List[Optional[_TensorMetadata]]

class _TensorMetadata:
    impl_ptr: Optional[int]
    storage_data_ptr: Optional[int]
    id: Optional[int]

class _ExtraFields_TorchOp:
    allow_tf32_cublas: bool
    inputs: _Inputs
    ...

class _ExtraFields_Backend: ...
class _ExtraFields_Allocation: ...
class _ExtraFields_OutOfMemory: ...

class _ExtraFields_PyCCall:
    caller: _PyFrameState
    ...

class _ExtraFields_PyCall:
    caller: _PyFrameState
    ...

class _ExtraFields_Kineto: ...

def _add_execution_graph_observer(output_file_path: str) -> bool: ...
def _remove_execution_graph_observer() -> None: ...
def _enable_execution_graph_observer() -> None: ...
def _disable_execution_graph_observer() -> None: ...
