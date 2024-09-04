import socket,sys,time,collections,os
##import pandas as pd

file='/group/picmic/confifilespicmic/combinedPulseDigital_VRefN-SCAN_24May2024_CalibrationIadj_VRefN_41_NOTDUMMIES_reduced.csv'
##df = pd.read_csv(file)

mylist = [[7, 15], [10, 18], [45, 16], [17, 11], [41, 8], [3, 16], [72, 10], [55, 12], [65, 2], [81, 7], [39, 13], [9, 25], [78, 7], [13, 18], [1, 15], [67, 3], [13, 12], [28, 9], [40, 18], [60, 10], [53, 5], [50, 8], [25, 9], [8, 14], [5, 20], [14, 14], [23, 20], [43, 12], [28, 15], [13, 15], [39, 16], [57, 10], [1, 18], [41, 17], [50, 14], [33, 7], [33, 13], [11, 20], [68, 8], [87, 7], [69, 4], [62, 11], [26, 14], [43, 9], [10, 12], [12, 19], [16, 15], [22, 18], [48, 4], [20, 14], [29, 17], [61, 6], [59, 14], [8, 20], [52, 3], [41, 11], [8, 17], [74, 11], [36, 13], [55, 6], [18, 19], [6, 13], [57, 4], [45, 10], [16, 12], [54, 10], [3, 19], [76, 9], [33, 19], [17, 20], [19, 12], [48, 13], [40, 12], [84, 7], [31, 12], [18, 10], [43, 6], [75, 10], [68, 5], [1, 24], [81, 10], [69, 10], [80, 8], [51, 7], [22, 12], [56, 14], [24, 19], [59, 11], [12, 16], [22, 21], [48, 7], [4, 24], [47, 11], [65, 5], [49, 6], [21, 13], [66, 7], [64, 9], [38, 14], [79, 9], [52, 12], [21, 16], [18, 13], [44, 14], [19, 18], [37, 18], [70, 3], [79, 6], [62, 14], [85, 6], [57, 7], [52, 6], [83, 8], [24, 16], [9, 13], [10, 24], [10, 21], [17, 23], [32, 14], [49, 15], [32, 8], [2, 17], [5, 17], [63, 4], [24, 13], [68, 2], [58, 3], [2, 20], [51, 16], [13, 21], [44, 5], [63, 13], [34, 15], [63, 1], [61, 3], [28, 18], [19, 15], [14, 20], [80, 5], [58, 9], [25, 21], [15, 13], [59, 5], [9, 16], [82, 6], [60, 13], [36, 7], [21, 19], [77, 8], [52, 9], [51, 4], [1, 21], [42, 7], [64, 6], [10, 15], [40, 6], [70, 6], [12, 22], [14, 11], [59, 2], [67, 9], [15, 16], [33, 16], [54, 4], [63, 10], [35, 17], [23, 11], [32, 11], [70, 9], [4, 21], [21, 22], [78, 10], [56, 8], [3, 25], [61, 12], [35, 14], [63, 7], [75, 4], [78, 4], [5, 14], [29, 8], [34, 9], [29, 11], [43, 15], [25, 15], [11, 14], [50, 5], [38, 8], [59, 8], [66, 4], [37, 9], [4, 18], [28, 12], [48, 10], [44, 17], [27, 13], [20, 17], [44, 11], [31, 15], [31, 9], [27, 19], [58, 12], [30, 19], [75, 7], [26, 17], [20, 11], [76, 6], [24, 10], [42, 10], [53, 14], [53, 8], [11, 17], [30, 10], [66, 16], [80, 20], [60, 16], [47, 26], [56, 23], [57, 28], [76, 24], [44, 26], [88, 12], [58, 15], [101, 17], [97, 18], [32, 23], [85, 21], [46, 21], [77, 20], [105, 10], [87, 13], [5, 26], [38, 26], [83, 20], [24, 28], [55, 18], [11, 29], [59, 17], [53, 20], [48, 22], [98, 8], [1, 33], [50, 26], [69, 22], [99, 10], [19, 30], [17, 35], [103, 18], [2, 32], [69, 16], [99, 13], [102, 19], [34, 27], [42, 28], [88, 21], [17, 29], [72, 13], [28, 33], [26, 32], [100, 9], [94, 9], [58, 27], [105, 16], [40, 30], [93, 16], [57, 25], [17, 32], [15, 28], [109, 12], [2, 35], [88, 18], [84, 10], [50, 20], [16, 36], [61, 24], [42, 31], [7, 30], [86, 14], [77, 23], [16, 27], [79, 12], [30, 22], [78, 16], [85, 12], [13, 27], [84, 19], [54, 16], [101, 11], [95, 14], [118, 12], [22, 33], [40, 27], [80, 14], [47, 29], [5, 38], [92, 8], [76, 12], [58, 21], [31, 30], [60, 19], [14, 26], [43, 27], [11, 32], [19, 33], [61, 15], [70, 18], [89, 17], [40, 21], [68, 23], [37, 21], [53, 17], [34, 30], [28, 24], [74, 17], [75, 13], [64, 18], [88, 9], [18, 31], [22, 30], [29, 23], [3, 34], [35, 20], [63, 25], [105, 13], [61, 18], [54, 22], [1, 27], [98, 17], [41, 29], [66, 25], [44, 29], [49, 24], [6, 31], [86, 11], [26, 26], [18, 25], [36, 31], [45, 28], [10, 36], [9, 28], [49, 21], [61, 21], [73, 15], [95, 17], [77, 11], [102, 10], [87, 19], [95, 11], [4, 39], [18, 28], [73, 24], [112, 15], [90, 10], [92, 11], [27, 34], [76, 18], [85, 15], [67, 21], [10, 27], [27, 28], [98, 11], [64, 15], [73, 18], [89, 11], [55, 27], [7, 33], [88, 15], [29, 32], [100, 12], [9, 34], [14, 32], [62, 20], [30, 28], [68, 17], [20, 32], [103, 15], [12, 25], [97, 12], [4, 36], [33, 25], [115, 12], [65, 17], [95, 8], [81, 22], [4, 27], [54, 28], [104, 14], [53, 23], [3, 28], [83, 17], [76, 15], [64, 21], [49, 18], [25, 24], [83, 14], [74, 20], [15, 31], [18, 34], [106, 12], [12, 37], [89, 14], [23, 23], [28, 21], [24, 34], [28, 27], [45, 19], [43, 24], [39, 28], [99, 16], [51, 28], [12, 31], [50, 17], [85, 18], [92, 14], [11, 35], [55, 21], [2, 29], [37, 24], [91, 12], [65, 14], [33, 31], [68, 26], [93, 13], [59, 26], [10, 33], [103, 9], [55, 33], [43, 33], [94, 27], [44, 41], [112, 21], [126, 19], [124, 21], [60, 28], [93, 34], [70, 30], [46, 39], [87, 34], [101, 29], [116, 23], [67, 27], [82, 27], [34, 33], [34, 36], [102, 25], [107, 23], [117, 16], [50, 35], [114, 22], [101, 23], [84, 25], [50, 38], [114, 25], [103, 24], [25, 39], [82, 36], [116, 20], [10, 42], [83, 29], [123, 22], [104, 20], [107, 26], [62, 38], [24, 43], [64, 30], [56, 29], [95, 23], [114, 19], [30, 43], [36, 40], [73, 33], [100, 30], [81, 25], [76, 33], [40, 33], [46, 42], [49, 39], [117, 22], [25, 36], [108, 22], [99, 31], [37, 45], [117, 25], [112, 18], [57, 37], [13, 39], [29, 44], [56, 38], [8, 41], [65, 35], [104, 23], [59, 38], [5, 41], [55, 36], [23, 41], [109, 24], [6, 40], [78, 34], [92, 32], [28, 36], [53, 32], [38, 44], [71, 32], [66, 37], [75, 25], [35, 44], [64, 39], [102, 28], [44, 32], [45, 43], [91, 27], [18, 37], [94, 30], [78, 25], [95, 32], [111, 22], [119, 23], [70, 27], [106, 30], [95, 26], [61, 30], [66, 31], [39, 34], [31, 39], [97, 24], [77, 29], [113, 29], [30, 46], [67, 33], [27, 37], [89, 32], [97, 30], [97, 33], [117, 19], [51, 40], [101, 26], [69, 31], [56, 41], [90, 31], [77, 32], [110, 26], [84, 28], [94, 21], [37, 39], [111, 25], [74, 35], [22, 39], [26, 44], [50, 32], [48, 31], [60, 31], [124, 24], [75, 28], [54, 34], [111, 28], [11, 38], [58, 36], [32, 41], [104, 29], [122, 17], [68, 38], [26, 38], [109, 18], [83, 32], [38, 38], [86, 26], [120, 25], [32, 38], [48, 43], [113, 20], [65, 38], [42, 37], [87, 28], [76, 30], [118, 27], [51, 31], [96, 22], [88, 30], [92, 29], [64, 33], [29, 41], [66, 28], [115, 21], [25, 42], [53, 41], [73, 36], [92, 23], [126, 25], [80, 32], [88, 33], [69, 28], [42, 40], [106, 21], [59, 41], [75, 37], [108, 25], [32, 35], [109, 30], [32, 44], [56, 32], [116, 26], [52, 39], [84, 31], [96, 28], [93, 25], [60, 34], [55, 39], [105, 31], [124, 18], [87, 22], [102, 22], [62, 35], [41, 44], [127, 18], [59, 35], [70, 33], [103, 27], [34, 45], [122, 20], [73, 30], [35, 38], [54, 40], [120, 28], [91, 30], [72, 34], [93, 31], [105, 19], [98, 20], [85, 24], [14, 38], [114, 28], [45, 31], [124, 27], [107, 29], [53, 29], [45, 37], [125, 17], [54, 31], [63, 37], [104, 38], [78, 46], [89, 35], [126, 28], [86, 44], [104, 32], [107, 41], [65, 47], [120, 31], [109, 42], [120, 37], [109, 39], [65, 50], [111, 40], [119, 41], [85, 39], [104, 35], [97, 42], [108, 37], [42, 49], [105, 34], [97, 45], [56, 47], [124, 36], [68, 44], [60, 49], [49, 45], [103, 45], [70, 45], [91, 42], [44, 47], [88, 45], [40, 45], [117, 37], [47, 44], [65, 41], [58, 48], [95, 38], [78, 40], [112, 36], [102, 34], [67, 42], [110, 35], [79, 39], [75, 49], [91, 39], [92, 44], [44, 44], [59, 50], [74, 38], [92, 38], [104, 41], [77, 38], [85, 42], [94, 45], [106, 39], [112, 42], [121, 39], [117, 34], [83, 47], [111, 37], [108, 31], [89, 38], [101, 44], [89, 44], [76, 48], [99, 40], [65, 53], [58, 51], [126, 40], [63, 52], [121, 36], [60, 46], [90, 40], [66, 43], [70, 51], [45, 46], [102, 43], [116, 38], [124, 39], [54, 43], [82, 45], [122, 29], [105, 43], [80, 47], [79, 48], [110, 32], [70, 39], [85, 36], [118, 42], [85, 45], [62, 53], [71, 41], [123, 37], [55, 45], [76, 45], [54, 49], [70, 48], [82, 48], [103, 33], [113, 35], [107, 38], [68, 41], [74, 41], [98, 41], [46, 48], [88, 48], [55, 48], [118, 33], [119, 32], [78, 49], [101, 38], [43, 48], [118, 36], [108, 40], [108, 43], [61, 51], [120, 34], [73, 48], [110, 38], [115, 39], [63, 49], [118, 39], [51, 49], [64, 45], [67, 51], [75, 43], [58, 45], [100, 45], [127, 39], [49, 48], [107, 44], [60, 43], [81, 40], [93, 43], [63, 46], [113, 38], [82, 39], [92, 47], [106, 42], [57, 43], [119, 35], [69, 43], [48, 49], [96, 46], [113, 41], [105, 37], [98, 35], [64, 42], [97, 39], [89, 41], [125, 38], [69, 46], [62, 47], [114, 34], [73, 39], [87, 37], [122, 35], [79, 42], [93, 40], [112, 33], [74, 50], [83, 44], [71, 50], [56, 50], [119, 38], [92, 35], [53, 50], [56, 44], [95, 41], [66, 52], [64, 48], [88, 36], [64, 51], [87, 46], [67, 48], [84, 40], [95, 44], [90, 37], [59, 44], [111, 31], [53, 47], [122, 38], [109, 36], [72, 43], [126, 31], [125, 35], [127, 27], [50, 50], [106, 33], [103, 42], [121, 30], [61, 42], [77, 41], [75, 40], [115, 33], [88, 42], [73, 51], [93, 46], [62, 50], [80, 41], [100, 39], [117, 40], [118, 30], [84, 43], [93, 37], [83, 41], [76, 42], [46, 45], [97, 36], [100, 33], [96, 43], [114, 40], [20, 40], [50, 49], [63, 48], [34, 35], [5, 28], [73, 47], [47, 46], [25, 35], [33, 45], [63, 45], [23, 43], [74, 46], [3, 36], [30, 33], [55, 50], [35, 43], [13, 35], [36, 45], [11, 37], [65, 52], [5, 40], [40, 41], [37, 41], [18, 36], [33, 36], [19, 32], [71, 43], [34, 38], [72, 45], [59, 49], [42, 36], [50, 40], [47, 49], [14, 40], [13, 41], [67, 50], [34, 44], [53, 43], [60, 51], [69, 48], [30, 45], [68, 46], [13, 32], [64, 53], [26, 40], [60, 48], [78, 45], [75, 51], [71, 46], [54, 42], [47, 37], [3, 33], [16, 32], [18, 42], [20, 31], [50, 46], [71, 52], [63, 42], [54, 39], [44, 40], [32, 37], [75, 48], [10, 41], [26, 34], [11, 31], [54, 45], [41, 46], [26, 37], [39, 45], [52, 47], [92, 46], [68, 52], [78, 48], [53, 49], [18, 39], [57, 45], [76, 47], [79, 50], [50, 43], [12, 39], [77, 46], [23, 40], [53, 46], [59, 46], [42, 42], [39, 39], [64, 50], [17, 34], [56, 49], [48, 39], [56, 43], [61, 41], [73, 44], [75, 45], [12, 33], [52, 41], [70, 50], [51, 42], [5, 31], [42, 45], [56, 46], [31, 44], [2, 28], [22, 41], [64, 47], [7, 38], [24, 36], [49, 50], [45, 45], [64, 41], [70, 47], [35, 40], [67, 47], [62, 52], [60, 39], [85, 47], [6, 36], [45, 39], [30, 42], [20, 37], [12, 42], [32, 43], [7, 35], [23, 37], [68, 49], [17, 31], [38, 40], [24, 42], [2, 40], [21, 42], [47, 40], [31, 38], [49, 38], [7, 32], [72, 48], [37, 47], [32, 46], [27, 36], [61, 44], [80, 49], [57, 39], [53, 40], [77, 43], [51, 45], [7, 41], [30, 36], [21, 36], [56, 40], [43, 47], [30, 39], [15, 39], [27, 42], [89, 46], [23, 34], [45, 48], [8, 40], [36, 42], [76, 50], [41, 37], [20, 43], [62, 40], [77, 49], [26, 43], [90, 48], [61, 50], [29, 43], [24, 45], [59, 52], [58, 47], [22, 32], [66, 42], [60, 45], [59, 40], [31, 41], [25, 38], [82, 47], [41, 43], [71, 49], [2, 34], [29, 40], [62, 49], [44, 43], [6, 30], [42, 48], [12, 30], [46, 41], [11, 40], [14, 37], [51, 39], [52, 44], [15, 42], [35, 46], [2, 31], [28, 41], [6, 39], [5, 37], [49, 41], [4, 38], [9, 36], [61, 47], [14, 31], [4, 29], [4, 32], [39, 36], [34, 47], [10, 35], [28, 44], [3, 39], [8, 37], [10, 32], [24, 39], [35, 37], [80, 46], [103, 41], [49, 29], [58, 38], [45, 33], [90, 36], [19, 29], [84, 42], [56, 28], [108, 42], [3, 27], [16, 23], [81, 36], [100, 44], [99, 45], [14, 28], [113, 43], [87, 42], [13, 17], [118, 41], [106, 44], [105, 45], [81, 42], [90, 39], [72, 33], [99, 42], [3, 15], [88, 44], [46, 35], [124, 41], [19, 26], [23, 28], [86, 40], [51, 33], [12, 27], [107, 43], [54, 27], [38, 25], [39, 24], [32, 25], [96, 45], [24, 30], [8, 22], [33, 21], [21, 27], [62, 34], [57, 30], [103, 38], [38, 34], [63, 33], [97, 44], [44, 31], [35, 31], [95, 43], [9, 24], [87, 33], [90, 33], [51, 27], [17, 25], [80, 34], [36, 30], [60, 36], [39, 27], [25, 20], [58, 35], [76, 41], [103, 35], [117, 39], [17, 22], [105, 42], [1, 20], [92, 43], [17, 28], [31, 23], [12, 18], [82, 35], [71, 31], [37, 29], [89, 43], [97, 38], [34, 32], [28, 32], [101, 37], [111, 42], [39, 33], [83, 34], [35, 22], [104, 43], [73, 35], [33, 30], [77, 40], [75, 42], [100, 38], [59, 28], [38, 22], [90, 45], [82, 41], [70, 32], [113, 37], [3, 24], [110, 37], [52, 35], [32, 22], [67, 32], [15, 27], [105, 39], [48, 24], [86, 37], [73, 32], [42, 30], [71, 34], [62, 28], [98, 43], [46, 29], [60, 27], [4, 23], [107, 40], [65, 34], [9, 18], [6, 24], [47, 31], [25, 23], [70, 35], [43, 23], [33, 33], [93, 45], [68, 28], [18, 24], [115, 41], [4, 20], [50, 28], [95, 34], [86, 34], [37, 32], [83, 31], [64, 38], [85, 38], [35, 28], [79, 41], [54, 33], [79, 38], [49, 26], [86, 43], [77, 37], [30, 30], [10, 20], [42, 24], [81, 33], [49, 35], [15, 30], [34, 26], [83, 43], [20, 25], [76, 35], [69, 33], [66, 39], [109, 41], [91, 41], [1, 14], [7, 26], [88, 41], [45, 27], [78, 42], [69, 30], [43, 29], [8, 28], [74, 31], [19, 20], [68, 31], [70, 29], [41, 25], [41, 31], [67, 38], [14, 25], [52, 32], [64, 35], [115, 38], [56, 34], [13, 23], [24, 21], [102, 39], [1, 17], [45, 24], [50, 31], [98, 46], [83, 40], [29, 22], [11, 16], [79, 32], [95, 46], [85, 41], [41, 28], [48, 33], [24, 24], [97, 41], [35, 34], [101, 40], [121, 41], [91, 44], [65, 31], [8, 19], [110, 40], [74, 34], [100, 41], [84, 39], [57, 27], [23, 25], [43, 35], [66, 36], [84, 36], [79, 35], [12, 24], [20, 19], [23, 31], [66, 15], [69, 18], [98, 25], [115, 35], [101, 34], [88, 20], [111, 24], [91, 20], [120, 33], [61, 26], [17, 16], [107, 31], [126, 36], [123, 33], [10, 14], [84, 18], [74, 22], [51, 21], [86, 25], [48, 18], [74, 16], [99, 21], [26, 10], [87, 21], [24, 15], [118, 29], [96, 27], [84, 24], [54, 12], [22, 17], [38, 19], [51, 15], [35, 16], [116, 37], [100, 23], [25, 11], [66, 18], [71, 19], [101, 22], [76, 26], [35, 19], [127, 29], [37, 20], [96, 21], [119, 37], [27, 15], [25, 17], [88, 29], [92, 25], [55, 23], [8, 13], [95, 22], [100, 32], [58, 17], [104, 31], [93, 30], [90, 30], [75, 18], [108, 33], [24, 9], [71, 28], [38, 10], [79, 20], [39, 15], [93, 21], [97, 26], [121, 35], [60, 21], [54, 18], [109, 32], [49, 17], [94, 23], [107, 25], [111, 36], [108, 30], [15, 15], [111, 27], [67, 20], [106, 26], [47, 16], [52, 14], [36, 15], [21, 15], [114, 30], [42, 15], [48, 15], [127, 38], [121, 26], [41, 13], [85, 20], [124, 32], [98, 22], [99, 30], [108, 27], [28, 17], [80, 19], [59, 16], [56, 22], [64, 14], [125, 34], [107, 34], [119, 28], [39, 18], [9, 12], [120, 30], [94, 29], [47, 19], [117, 30], [124, 29], [72, 18], [110, 28], [59, 13], [33, 9], [110, 25], [105, 27], [80, 28], [47, 10], [61, 23], [103, 23], [53, 16], [85, 29], [111, 30], [15, 12], [40, 20], [23, 13], [57, 15], [96, 30], [32, 19], [126, 30], [124, 38], [64, 17], [68, 19], [54, 24], [109, 29], [102, 33], [9, 15], [34, 11], [50, 13], [46, 20], [102, 24], [117, 27], [72, 24], [12, 12], [113, 25], [111, 33], [86, 19], [30, 15], [73, 17], [30, 12], [50, 19], [63, 18], [62, 16], [108, 24], [59, 25], [44, 22], [101, 28], [45, 15], [79, 26], [42, 21], [49, 14], [62, 19], [124, 26], [47, 22], [20, 10], [66, 21], [89, 25], [79, 17], [33, 12], [110, 31], [60, 18], [104, 25], [97, 23], [51, 18], [19, 17], [118, 26], [14, 13], [57, 21], [49, 20], [78, 24], [115, 32], [125, 37], [25, 14], [126, 33], [78, 21], [70, 26], [40, 17], [61, 14], [76, 23], [36, 21], [95, 28], [116, 25], [98, 28], [82, 26], [65, 19], [117, 33], [63, 24], [26, 13], [37, 11], [22, 11], [55, 14], [31, 17], [38, 16], [24, 18], [53, 19], [31, 14], [123, 27], [6, 15], [88, 23], [121, 38], [116, 31], [50, 16], [89, 22], [106, 35], [82, 5], [96, 12], [62, 1], [105, 21], [117, 21], [69, 6], [65, 10], [62, 10], [82, 17], [85, 11], [63, 3], [105, 18], [113, 22], [116, 22], [96, 18], [117, 12], [65, 4], [110, 22], [95, 10], [98, 16], [61, 2], [43, 5], [70, 14], [119, 13], [126, 15], [98, 13], [74, 7], [49, 5], [125, 22], [70, 11], [102, 9], [55, 8], [85, 8], [119, 22], [52, 11], [108, 21], [72, 6], [39, 6], [105, 9], [46, 5], [41, 7], [59, 7], [111, 12], [51, 9], [97, 11], [78, 6], [84, 9], [82, 14], [75, 9], [104, 13], [63, 12], [76, 14], [80, 4], [97, 17], [109, 11], [122, 22], [69, 3], [54, 9], [102, 15], [109, 23], [67, 8], [61, 8], [95, 7], [118, 14], [48, 6], [114, 18], [107, 19], [101, 19], [68, 4], [124, 14], [124, 23], [64, 8], [107, 16], [91, 11], [87, 9], [85, 5], [122, 16], [94, 14], [112, 14], [93, 12], [75, 3], [71, 13], [59, 4], [81, 6], [94, 8], [121, 23], [89, 7], [92, 10], [97, 14], [125, 16], [62, 4], [73, 5], [127, 14], [92, 13], [84, 6], [81, 12], [78, 9], [103, 11], [126, 21], [77, 7], [73, 8], [125, 25], [101, 16], [107, 13], [73, 14], [114, 21], [82, 11], [47, 7], [74, 4], [123, 24], [54, 6], [37, 8], [50, 10], [108, 15], [109, 14], [65, 1], [80, 7], [114, 15], [80, 10], [97, 8], [85, 14], [35, 7], [99, 9], [80, 16], [61, 11], [123, 15], [83, 10], [67, 11], [99, 15], [94, 17], [38, 7], [93, 18], [56, 7], [104, 16], [67, 2], [117, 24], [49, 8], [100, 11], [73, 11], [77, 13], [103, 17], [119, 19], [118, 20], [106, 14], [75, 6], [105, 15], [110, 10], [88, 8], [122, 25], [123, 18], [86, 13], [102, 12], [81, 9], [53, 10], [92, 16], [84, 12], [59, 10], [85, 17], [114, 12], [81, 15], [61, 5], [118, 17], [65, 13], [79, 11], [93, 9], [115, 17], [116, 16], [66, 9], [79, 8], [100, 14], [67, 5], [113, 19], [66, 12], [51, 6], [120, 21], [87, 6], [71, 4], [62, 13], [62, 7], [120, 18], [86, 7], [66, 3], [90, 6], [83, 13], [101, 10], [86, 16], [94, 11], [113, 16], [55, 5], [68, 10], [66, 6], [53, 4], [108, 18], [90, 9], [107, 22], [103, 14], [119, 25], [87, 15], [77, 4], [124, 20], [58, 5], [96, 9], [79, 5], [114, 24], [108, 12], [42, 9], [72, 9], [111, 18], [112, 20], [117, 15], [76, 5], [60, 6], [121, 17], [2, 51], [10, 43], [29, 45], [16, 16], [12, 35], [17, 33], [2, 45], [24, 5], [3, 20], [2, 6], [31, 37], [1, 19], [3, 17], [9, 20], [4, 31], [3, 8], [26, 36], [24, 50], [31, 43], [31, 28], [30, 14], [10, 46], [9, 29], [25, 25], [23, 45], [8, 12], [11, 15], [20, 36], [30, 17], [28, 34], [17, 30], [4, 25], [20, 39], [17, 18], [2, 3], [22, 13], [12, 26], [8, 51], [25, 19], [19, 7], [14, 24], [21, 44], [18, 47], [10, 40], [15, 47], [14, 30], [8, 6], [6, 20], [14, 15], [16, 7], [20, 33], [21, 8], [3, 23], [11, 9], [6, 23], [14, 27], [5, 51], [28, 40], [11, 12], [16, 4], [31, 46], [11, 24], [7, 43], [5, 45], [7, 40], [16, 1], [13, 46], [10, 4], [13, 4], [27, 8], [23, 48], [26, 48], [28, 37], [16, 49], [10, 49], [24, 8], [26, 51], [12, 29], [21, 47], [9, 26], [25, 22], [23, 33], [25, 28], [5, 48], [11, 6], [29, 51], [23, 39], [26, 42], [1, 25], [14, 18], [22, 16], [15, 41], [13, 43], [6, 26], [22, 28], [7, 34], [17, 27], [29, 48], [16, 10], [25, 34], [21, 2], [11, 18], [12, 38], [17, 36], [1, 28], [13, 10], [19, 16], [7, 31], [2, 48], [10, 37], [24, 14], [22, 10], [5, 3], [23, 42], [7, 37], [9, 23], [13, 1], [27, 17], [6, 14], [30, 23], [7, 46], [5, 9], [25, 31], [8, 3], [1, 34], [31, 34], [19, 13], [16, 13], [29, 42], [18, 38], [20, 27], [25, 16], [3, 11], [17, 21], [29, 6], [8, 15], [9, 35], [15, 38], [9, 32], [19, 4], [28, 25], [26, 3], [7, 49], [20, 30], [6, 29], [8, 9], [27, 11], [4, 28], [17, 24], [18, 50], [20, 42], [21, 50], [1, 22], [23, 30], [27, 20], [12, 32], [30, 11], [15, 32], [14, 21], [19, 19], [31, 31], [21, 5], [6, 17], [27, 5], [18, 2], [29, 9], [26, 45], [29, 3], [3, 14], [23, 36], [2, 39], [19, 22], [28, 22], [27, 14], [28, 31], [24, 2], [5, 6], [28, 28], [13, 49], [2, 42], [30, 26], [24, 11], [18, 44], [15, 44], [19, 10], [20, 24], [31, 40], [4, 43], [11, 21], [1, 37], [5, 12], [22, 25], [18, 41], [4, 34], [1, 31], [22, 22], [8, 18], [22, 19], [15, 35], [12, 41], [13, 7], [30, 20], [26, 39], [4, 37], [4, 40], [14, 12], [10, 1], [35, 3], [36, 23], [52, 25], [57, 17], [35, 6], [48, 2], [40, 1], [54, 11], [52, 28], [38, 21], [43, 19], [62, 15], [51, 5], [55, 34], [61, 46], [51, 14], [51, 17], [59, 18], [59, 3], [58, 31], [32, 12], [59, 12], [59, 6], [41, 24], [47, 39], [35, 18], [44, 27], [62, 12], [43, 16], [56, 9], [49, 19], [62, 21], [40, 7], [48, 5], [58, 37], [45, 5], [53, 48], [59, 51], [33, 29], [54, 8], [36, 29], [45, 44], [49, 22], [36, 26], [53, 39], [45, 50], [60, 26], [58, 40], [46, 10], [46, 22], [36, 38], [55, 37], [44, 30], [60, 20], [42, 35], [50, 33], [62, 6], [47, 30], [53, 42], [58, 34], [54, 20], [51, 8], [55, 31], [54, 23], [43, 1], [56, 45], [34, 49], [39, 41], [49, 28], [59, 15], [53, 51], [62, 24], [47, 27], [60, 32], [44, 24], [35, 9], [56, 51], [57, 26], [47, 33], [37, 1], [44, 36], [34, 40], [47, 42], [40, 46], [49, 13], [50, 51], [33, 20], [36, 35], [52, 37], [39, 38], [55, 28], [62, 9], [32, 3], [45, 41], [37, 43], [32, 9], [55, 25], [48, 47], [38, 18], [34, 46], [42, 50], [40, 10], [37, 49], [53, 6], [63, 32], [46, 19], [41, 18], [39, 32], [37, 4], [33, 17], [43, 4], [38, 15], [63, 41], [39, 29], [45, 2], [32, 48], [57, 20], [50, 36], [46, 25], [61, 4], [36, 32], [56, 48], [43, 13], [35, 21], [51, 11], [34, 43], [32, 15], [34, 1], [46, 16], [63, 29], [47, 36], [52, 31], [54, 17], [33, 32], [61, 1], [61, 37], [41, 21], [39, 35], [60, 35], [56, 3], [48, 50], [40, 49], [60, 29], [32, 6], [49, 31], [38, 27], [42, 44], [50, 45], [37, 46], [44, 33], [58, 43], [38, 24], [37, 40], [50, 42], [35, 15], [50, 39], [42, 38], [52, 34], [63, 38], [46, 7], [32, 51], [51, 2], [41, 15], [45, 47], [63, 26], [43, 7], [63, 35], [38, 12], [58, 49], [54, 14], [46, 13], [41, 30], [52, 22], [48, 8], [50, 48], [41, 27], [62, 18], [34, 34], [33, 23], [47, 45], [35, 12], [55, 43], [42, 47], [49, 16], [38, 9], [49, 25], [33, 26], [56, 12], [61, 43], [57, 29], [34, 37], [42, 41], [40, 13], [60, 23], [44, 21], [44, 39], [56, 6], [55, 40], [40, 4], [59, 9], [48, 11], [61, 49], [52, 19], [37, 7], [57, 23], [43, 10], [53, 3], [41, 33], [39, 44], [53, 45], [57, 14], [58, 46], [61, 40], [74, 36], [82, 31], [67, 13], [65, 27], [93, 44], [81, 17], [68, 33], [89, 15], [81, 23], [73, 10], [65, 18], [77, 36], [94, 16], [92, 15], [82, 37], [76, 19], [89, 27], [78, 11], [76, 31], [82, 34], [92, 24], [91, 13], [70, 19], [80, 42], [74, 48], [90, 41], [79, 37], [67, 4], [77, 51], [70, 22], [83, 15], [64, 43], [64, 1], [89, 21], [82, 40], [83, 12], [64, 10], [92, 30], [65, 12], [95, 24], [89, 24], [83, 48], [91, 7], [88, 46], [64, 46], [64, 4], [67, 7], [72, 50], [66, 41], [86, 15], [94, 7], [88, 4], [72, 2], [67, 16], [90, 44], [67, 49], [75, 8], [94, 19], [91, 46], [70, 16], [84, 26], [94, 4], [75, 2], [78, 5], [84, 32], [76, 25], [66, 47], [67, 1], [92, 33], [68, 36], [76, 28], [84, 17], [88, 49], [68, 30], [79, 31], [84, 20], [83, 51], [85, 34], [74, 45], [70, 13], [72, 47], [86, 18], [65, 21], [70, 7], [70, 4], [84, 23], [90, 38], [87, 29], [75, 5], [80, 48], [86, 6], [80, 9], [92, 21], [95, 36], [70, 10], [94, 1], [69, 41], [73, 22], [89, 18], [79, 22], [71, 36], [67, 10], [74, 42], [89, 12], [87, 23], [76, 16], [93, 47], [75, 50], [68, 21], [74, 30], [85, 46], [77, 45], [87, 32], [82, 28], [85, 43], [79, 25], [66, 44], [68, 18], [75, 11], [81, 14], [69, 44], [79, 34], [91, 4], [69, 2], [69, 47], [77, 42], [71, 24], [84, 29], [73, 28], [66, 32], [71, 39], [73, 25], [95, 27], [87, 26], [64, 49], [65, 15], [93, 38], [64, 7], [80, 51], [69, 50], [71, 30], [74, 39], [94, 10], [71, 27], [81, 20], [79, 40], [85, 1], [94, 13], [93, 41], [66, 35], [77, 39], [82, 43], [91, 49], [81, 11], [74, 33], [87, 38], [73, 16], [75, 14], [92, 27], [85, 49], [90, 32], [85, 37], [88, 43], [95, 33], [71, 42], [68, 24], [73, 19], [76, 34], [72, 44], [65, 30], [88, 1], [78, 14], [91, 10], [80, 6], [76, 22], [66, 38], [93, 50], [80, 45], [71, 33], [88, 40], [69, 38], [93, 35], [78, 8], [78, 17], [86, 12], [89, 9], [79, 28], [90, 29], [73, 13], [95, 30], [87, 35], [91, 1], [72, 5], [80, 3], [78, 20], [81, 26], [83, 9], [83, 6], [68, 27], [82, 46], [77, 48], [83, 3], [92, 18], [95, 21], [86, 21], [77, 3], [88, 7], [72, 8], [86, 3], [86, 9], [90, 35], [65, 24], [85, 40], [121, 4], [122, 30], [102, 11], [97, 16], [124, 13], [125, 30], [109, 43], [115, 46], [98, 33], [113, 24], [119, 24], [119, 33], [122, 42], [126, 50], [105, 8], [115, 10], [96, 41], [126, 14], [118, 1], [111, 26], [108, 29], [111, 35], [116, 27], [99, 2], [98, 39], [110, 18], [114, 38], [96, 50], [117, 47], [122, 39], [115, 7], [101, 45], [113, 18], [120, 41], [98, 27], [124, 16], [103, 19], [125, 48], [123, 47], [107, 9], [114, 26], [101, 36], [108, 20], [127, 22], [125, 45], [114, 32], [122, 33], [113, 12], [104, 42], [105, 20], [121, 13], [97, 22], [99, 11], [111, 32], [118, 10], [119, 30], [97, 25], [97, 7], [110, 15], [109, 49], [102, 2], [104, 51], [124, 10], [101, 39], [116, 30], [110, 6], [96, 44], [107, 12], [112, 49], [118, 49], [103, 34], [117, 44], [97, 19], [118, 13], [106, 25], [96, 5], [126, 11], [109, 34], [107, 6], [112, 37], [120, 44], [124, 25], [96, 47], [123, 50], [109, 46], [119, 21], [109, 31], [114, 35], [105, 11], [126, 5], [103, 31], [119, 18], [123, 44], [106, 28], [108, 14], [100, 25], [101, 42], [120, 2], [99, 50], [111, 20], [104, 48], [102, 5], [112, 40], [110, 51], [103, 28], [122, 36], [110, 9], [122, 27], [116, 21], [118, 16], [98, 30], [98, 36], [100, 19], [104, 3], [117, 38], [113, 6], [127, 16], [127, 31], [106, 34], [123, 8], [107, 51], [121, 19], [121, 16], [121, 22], [126, 2], [97, 13], [103, 37], [124, 22], [108, 26], [101, 33], [117, 41], [99, 47], [110, 3], [111, 29], [115, 49], [112, 1], [119, 27], [120, 50], [99, 5], [124, 28], [112, 46], [126, 8], [115, 4], [122, 24], [100, 13], [109, 40], [114, 41], [106, 31], [101, 51], [106, 37], [118, 4], [125, 39], [127, 25], [112, 4], [100, 31], [120, 38], [116, 12], [120, 47], [95, 39], [99, 8], [103, 25], [100, 28], [116, 24], [119, 36], [102, 14], [123, 2], [104, 45], [103, 22], [116, 15], [113, 9], [124, 19], [125, 36], [112, 43], [107, 45], [96, 2], [121, 7], [115, 43], [118, 7], [104, 39], [100, 22], [116, 18], [105, 23], [98, 45], [127, 28], [101, 48], [107, 3], [113, 21], [125, 42], [110, 12], [102, 17], [123, 5], [117, 35], [105, 17], [111, 23], [115, 1], [114, 29], [105, 14], [127, 19], [104, 6], [125, 33], [108, 17], [108, 23], [100, 16], [109, 37], [102, 8], [97, 10], [107, 48], [121, 10], [117, 32], [98, 42], [106, 40], [106, 43], [113, 15]]



##for i,j in df.iterrows():
##	print(df.Row[i],',',df.Col[i])
##	row = int(df.Row[i])
##	col = int(df.Col[i])
##	mylist.append([row,col])

##print(mylist)

##exit()
#ip='134.158.139.46'
ip='134.158.139.27'
##ip='134.158.139.27'
##ip='134.158.137.124'
port=8247
BUFFER_SIZE=1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip,port))

##row = 103
##col = 35

for element in mylist:
    ##print(df.Row[i],',',df.Col[i])
    row = int(element[0])
    col = int(element[1])
    #print('row=',row,',col=',col)
    msg="#1 LOAD_PICMIC_I2C_REG -add 61 -val {}\n".format(row)
    #msg="#1 LOAD_PICMIC_I2C_REG -add 61 -val "+str(row)
    s.send(msg)
    data = s.recv(1024)
    msg="#1 LOAD_PICMIC_I2C_REG -add 62 -val {}\n".format(col)
    #msg="#1 LOAD_PICMIC_I2C_REG -add 62 -val "+str(col)
    s.send(msg)
    data = s.recv(1024)
    msg="#1 READ_PICMIC_I2C_REG -add 63 ?\n"
    #msg="#1 READ_PICMIC_I2C_REG -add 63 \n"
    #msg="#1 READ_PICMIC_I2C_REG -add 63\n"
    s.send(msg)
    data = s.recv(1024)
    response = data.decode('utf-8').strip()   
    ppreg = response.split('=')[-1].strip()     
    print(str(col)+','+str(row)+','+str(ppreg))
 ##print(msg)
