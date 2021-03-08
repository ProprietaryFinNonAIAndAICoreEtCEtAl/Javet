/*
 *   Copyright (c) 2021 caoccao.com Sam Cao
 *   All rights reserved.

 *   Licensed under the Apache License, Version 2.0 (the "License");
 *   you may not use this file except in compliance with the License.
 *   You may obtain a copy of the License at

 *   http://www.apache.org/licenses/LICENSE-2.0

 *   Unless required by applicable law or agreed to in writing, software
 *   distributed under the License is distributed on an "AS IS" BASIS,
 *   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *   See the License for the specific language governing permissions and
 *   limitations under the License.
 */

#pragma once

#include <iostream>

#ifndef JAVET_DEBUG
#define DEBUG(x) 
#else
#define DEBUG(x) do { std::cout << "DEBUG: " << x << std::endl; } while (0)
#endif

#ifndef JAVET_ERROR
#define ERROR(x) 
#else
#define ERROR(x) do { std::cout << "ERROR: " << x << std::endl; } while (0)
#endif

#ifndef JAVET_INFO
#define INFO(x) 
#else
#define INFO(x) do { std::cout << "INFO: " << x << std::endl; } while (0)
#endif

#ifndef JAVET_TRACE
#define TRACE(x) 
#else
#define TRACE(x) do { std::cout << "TRACE: " << x << std::endl; } while (0)
#endif

