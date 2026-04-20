# CNN Configuration

## Overview
Configuring a CNN involves designing the architecture (layers, filters, connections) and setting training hyperparameters.

---

## CNN Architecture Components

### 1. Convolutional Layer
```
Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0)
```

**Key decisions:**
- **Kernel size**: 3×3 (standard), 5×5, 7×7 (early layers)
- **Stride**: 1 (preserve size), 2 (downsample)
- **Padding**: 0 (valid), 1 for 3×3 kernel (same)
- **Output channels**: Powers of 2 (32, 64, 128, 256, 512)

### 2. Pooling Layer
```
MaxPool2d(kernel_size=2, stride=2)    // Most common
AvgPool2d(kernel_size=2, stride=2)   // For final layers
AdaptiveAvgPool2d(output_size=1)     // Global pooling
```

### 3. Activation Function
- **ReLU**: Default choice (fast, no vanishing gradient)
- **LeakyReLU**: For GANs/deep networks
- **GELU**: Modern alternative (Vision Transformers)

### 4. Normalization
- **BatchNorm**: Standard for CNNs
- **LayerNorm**: Used in Transformers

---

## Standard CNN Configuration Template

```
Algorithm ConfigureCNN(input_shape, num_classes, architecture_type="standard")
Input:
    - input_shape: (C, H, W) - channels, height, width
    - num_classes: number of output classes
    - architecture_type: "shallow", "standard", "deep", "resnet"

Output:
    - model: configured CNN architecture

// ============================================
// CONFIGURATION PARAMETERS
// ============================================
1. C, H, W ← input_shape

2. // Choose architecture parameters
3. SWITCH architecture_type:
4.     CASE "shallow":           // For small datasets
5.         conv_layers ← [(32, 3), (64, 3)]
6         fc_units ← [128]
7.         dropout ← 0.3
8.         
9.     CASE "standard":          // Default
10.        conv_layers ← [(32, 3), (64, 3), (128, 3), (256, 3)]
11.        fc_units ← [512, 256]
12.        dropout ← 0.5
13.        
14.    CASE "deep":              // For large datasets
15.        conv_layers ← [(64, 3), (64, 3), (128, 3), (128, 3), 
16.                       (256, 3), (256, 3), (512, 3)]
17.        fc_units ← [1024, 512, 256]
18.        dropout ← 0.5
19.        
20.    CASE "resnet":            // ResNet-style
21.        RETURN ConfigureResNet(input_shape, num_classes)

// ============================================
// BUILD CONVOLUTIONAL FEATURE EXTRACTOR
// ============================================
22. layers ← []
23. in_channels ← C
24. 
25. FOR (out_channels, kernel_size) IN conv_layers DO:
26.     
27.     // Convolution
28.     APPEND(layers, Conv2d(in_channels, out_channels, 
29.                           kernel_size, padding=kernel_size//2))
30.     
31.     // Normalization
32.     APPEND(layers, BatchNorm2d(out_channels))
33.     
34.     // Activation
35.     APPEND(layers, ReLU())
36.     
37.     // Pooling every 1-2 conv layers
38.     APPEND(layers, MaxPool2d(kernel_size=2, stride=2))
39.     
40.     in_channels ← out_channels
41. END FOR

// ============================================
// GLOBAL POOLING / FLATTENING
// ============================================
42. // Option 1: Global Average Pooling (preferred)
43. APPEND(layers, AdaptiveAvgPool2d(output_size=1))
44. flatten_size ← out_channels    // After global pooling
45. 
46. // Option 2: Flatten (alternative)
47. // flatten_size ← out_channels × (H // 2^num_pooling) × (W // 2^num_pooling)

// ============================================
// BUILD CLASSIFIER (Fully Connected)
// ============================================
48. classifier ← []
49. in_features ← flatten_size
50. 
51. FOR units IN fc_units DO:
52.     APPEND(classifier, Linear(in_features, units))
53.     APPEND(classifier, ReLU())
54.     APPEND(classifier, Dropout(p=dropout))
55.     in_features ← units
56. END FOR
57. 
58. // Output layer
59. APPEND(classifier, Linear(in_features, num_classes))
60. 
61. RETURN {features: layers, classifier: classifier}
```

---

## Training Configuration

```
Algorithm ConfigureTraining(model, dataset_size, task="classification")
Input:
    - model: CNN model
    - dataset_size: number of training samples
    - task: "classification", "segmentation", "detection"

Output:
    - training_config: hyperparameters and settings

// ============================================
// OPTIMIZER CONFIGURATION
// ============================================
1. IF dataset_size < 10000 THEN:
2.     optimizer ← "SGD"
3.     learning_rate ← 0.01
4.     momentum ← 0.9
5.     weight_decay ← 5e-4
6. ELSE:
7.     optimizer ← "Adam"
8.     learning_rate ← 0.001
9.     betas ← (0.9, 0.999)
10.    weight_decay ← 1e-4
11. END IF

// ============================================
// LEARNING RATE SCHEDULE
// ============================================
12. scheduler ← "StepLR"
13. step_size ← 30    // epochs
14. gamma ← 0.1       // multiply LR by this every step_size epochs

// Alternative: CosineAnnealing
// scheduler ← "CosineAnnealingLR"
// T_max ← num_epochs

// ============================================
// BATCH SIZE
// ============================================
15. IF dataset_size < 1000 THEN:
16.     batch_size ← 16
17. ELSE IF dataset_size < 10000 THEN:
18.     batch_size ← 32
19. ELSE IF dataset_size < 100000 THEN:
20.     batch_size ← 64
21. ELSE:
22.     batch_size ← 128
23. END IF

// ============================================
// LOSS FUNCTION
// ============================================
24. SWITCH task:
25.     CASE "classification":
26.         IF num_classes == 2 THEN:
27.             loss_fn ← "BCEWithLogitsLoss"
28.         ELSE:
29.             loss_fn ← "CrossEntropyLoss"
30.         END IF
31.         
32.     CASE "segmentation":
33.         loss_fn ← "CrossEntropyLoss"  // or "DiceLoss"
34.         
35.     CASE "detection":
36.         loss_fn ← "MultiTaskLoss"    // Classification + Regression

// ============================================
// DATA AUGMENTATION
// ============================================
37. train_transforms ← [
38.     RandomHorizontalFlip(p=0.5),
39.     RandomRotation(degrees=15),
40.     ColorJitter(brightness=0.2, contrast=0.2),
41.     Normalize(mean=DATASET_MEAN, std=DATASET_STD)
42. ]

43. val_transforms ← [
44.     Normalize(mean=DATASET_MEAN, std=DATASET_STD)
45. ]

// ============================================
// TRAINING LOOP SETTINGS
// ============================================
46. num_epochs ← 100
47. early_stopping_patience ← 10
48. gradient_clip_value ← 1.0    // For preventing exploding gradients

49. RETURN {
50.     optimizer: optimizer,
51.     learning_rate: learning_rate,
52.     scheduler: scheduler,
53.     batch_size: batch_size,
54.     loss_fn: loss_fn,
55.     num_epochs: num_epochs,
56.     train_transforms: train_transforms,
57.     val_transforms: val_transforms,
58.     early_stopping: early_stopping_patience,
59.     gradient_clip: gradient_clip_value
60. }
```

---

## Common Architecture Patterns

### VGG-Style (Sequential)
```
Conv(3, 64) → Conv(64, 64) → Pool
→ Conv(64, 128) → Conv(128, 128) → Pool
→ Conv(128, 256) → Conv(256, 256) → Pool
→ FC(512) → FC(num_classes)
```

### ResNet-Style (Skip Connections)
```
Input → Conv → BN → ReLU → MaxPool
→ ResBlock × 2 (64 filters)
→ ResBlock × 2 (128 filters, stride=2)
→ ResBlock × 2 (256 filters, stride=2)
→ ResBlock × 2 (512 filters, stride=2)
→ GlobalAvgPool → FC(num_classes)
```

ResBlock:
```
Input → Conv → BN → ReLU → Conv → BN → (+ Input) → ReLU
```

---

## Output Size Calculation

```
Formula for conv output:
    output_size = floor((input_size + 2×padding - kernel_size) / stride) + 1

Formula for pooling output:
    output_size = floor(input_size / stride)

Example: 224×224 input with 3 Conv+Pool blocks
    Block 1: 224 → 112 (after 3×3 conv, stride 1, pad 1 + 2×2 pool, stride 2)
    Block 2: 112 → 56
    Block 3: 56 → 28
    Final feature map: 28×28
```

---

## Transfer Learning Configuration

```
Algorithm ConfigureTransferLearning(base_model, num_classes, 
                                     freeze_strategy="partial")
Input:
    - base_model: pretrained model (e.g., ResNet50)
    - num_classes: new number of classes
    - freeze_strategy: "none", "partial", "all"

Output:
    - model: configured model for fine-tuning

1. // Replace final layer
2. num_features ← base_model.fc.in_features
3. base_model.fc ← Linear(num_features, num_classes)

4. // Freeze strategy
5. SWITCH freeze_strategy:
6.     CASE "all":
7.         FOR param IN base_model.parameters() EXCEPT fc:
8.             param.requires_grad ← FALSE
9.             
10.    CASE "partial":
11.        // Freeze early layers, train later layers
12.        FOR layer IN base_model.layers[:4]:
13.            FOR param IN layer.parameters():
14.                param.requires_grad ← FALSE
15.                
16.    CASE "none":
17.        // Train all layers
18.        pass

19. // Different learning rates
20. optimizer ← Adam([
21.     {'params': base_model.fc.parameters(), 'lr': 0.001},
22.     {'params': base_model.layer4.parameters(), 'lr': 0.0001},
23.     {'params': base_model.earlier_layers.parameters(), 'lr': 0.00001}
24. ])

25. RETURN base_model
```

---

## Quick Reference: Layer Choices

| Layer Type | When to Use | Typical Values |
|------------|-------------|----------------|
| Conv 3×3 | Default choice | stride=1, padding=1 |
| Conv 1×1 | Dimension reduction | Bottleneck layers |
| Conv 5×5 | Early layers (receptive field) | First layer only |
| MaxPool 2×2 | Downsampling | stride=2 |
| GlobalAvgPool | Final layer before FC | output=1 |
| BatchNorm | After every conv | Default settings |
| Dropout | Before FC layers | p=0.3-0.5 |

---

## Python Implementation (PyTorch)
```python
import torch.nn as nn

class SimpleCNN(nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        
        # Feature extractor
        self.features = nn.Sequential(
            nn.Conv2d(3, 64, 3, padding=1),
            nn.BatchNorm2d(64),
            nn.ReLU(),
            nn.MaxPool2d(2),
            
            nn.Conv2d(64, 128, 3, padding=1),
            nn.BatchNorm2d(128),
            nn.ReLU(),
            nn.MaxPool2d(2),
            
            nn.Conv2d(128, 256, 3, padding=1),
            nn.BatchNorm2d(256),
            nn.ReLU(),
            nn.AdaptiveAvgPool2d(1)
        )
        
        # Classifier
        self.classifier = nn.Sequential(
            nn.Flatten(),
            nn.Linear(256, 128),
            nn.ReLU(),
            nn.Dropout(0.5),
            nn.Linear(128, num_classes)
        )
    
    def forward(self, x):
        x = self.features(x)
        x = self.classifier(x)
        return x
```
