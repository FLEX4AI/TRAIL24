"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/03_compression.onnx.ipynb.

# %% auto 0
__all__ = ['script_model', 'quantize_onnx']

# %% ../../nbs/03_compression.onnx.ipynb 3
import torch
import torch.nn as nn
from onnxruntime.quantization import quantize_dynamic, QuantType

# %% ../../nbs/03_compression.onnx.ipynb 4
def script_model(model, dummy_input, path='scripted_model.pt'):
    scripted_model = torch.jit.trace(model, dummy_input)
    scripted_model.save(path)
    return scripted_model

# %% ../../nbs/03_compression.onnx.ipynb 5
def quantize_onnx(model, dummy_input, onnx_path="model.onnx", quant_onnx_path="model_quantized.onnx"):
    torch.onnx.export(
    model,              
    dummy_input,        
    onnx_path, 
    input_names=["features", "year", "month", "day", "hour"],   
    output_names=["output"], 
    dynamic_axes={"input": {0: "batch_size"}, "output": {0: "batch_size"}}, 
    opset_version=11
    )

    quantize_dynamic(
        onnx_path,
        quant_onnx_path,
        weight_type=QuantType.QUInt8
    )
