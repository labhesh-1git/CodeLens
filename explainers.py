import re
import ast
from typing import Dict, List, Any

class CodeExplainer:
    """
    F1-themed AI Code Explainer Engine
    Provides comprehensive code analysis like a racing team's telemetry system
    """
    
    def __init__(self):
        self.keywords = {
            'def': 'Function definition keyword - declares a new function (like designing a new F1 car component)',
            'if': 'Conditional statement - creates decision points in code execution (like choosing pit strategy)',
            'else': 'Alternative condition - executes when if-condition is false (backup race strategy)',
            'elif': 'Additional condition - chain multiple conditions (multiple strategy options)',
            'for': 'Loop statement - repeats code for each item in sequence (like laps in a race)',
            'while': 'Loop statement - repeats code while condition is true (racing until checkered flag)',
            'return': 'Function output - sends result back to caller (like telemetry data to pit crew)',
            'import': 'Module inclusion - brings external code libraries (like importing racing regulations)',
            'from': 'Selective import - imports specific parts from module (choosing specific F1 regulations)',
            'class': 'Object blueprint - defines structure for creating objects (F1 car chassis design)',
            'try': 'Error handling - attempts risky code execution (trying aggressive overtake maneuver)',
            'except': 'Error catching - handles exceptions gracefully (damage control after incident)',
            'finally': 'Cleanup code - always executes regardless of errors (post-race procedures)',
            'with': 'Context manager - ensures proper resource handling (pit crew safety protocols)',
            'lambda': 'Anonymous function - creates small inline functions (quick pit radio instructions)',
            'yield': 'Generator output - produces values on demand (streaming race data)',
            'break': 'Loop exit - immediately stops loop execution (retiring from race)',
            'continue': 'Loop skip - skips to next iteration (skipping damaged sector)',
            'pass': 'Placeholder - does nothing, used for empty code blocks (placeholder for future development)',
            'global': 'Global scope - accesses variables from outer scope (team-wide communication)',
            'nonlocal': 'Enclosing scope - accesses variables from enclosing function (driver-engineer communication)',
            'assert': 'Debugging check - verifies conditions during development (safety systems check)',
            'del': 'Object deletion - removes references to objects (removing old car components)',
            'in': 'Membership test - checks if item exists in sequence (checking if driver is in points)',
            'is': 'Identity test - checks if two variables reference same object (same car chassis)',
            'not': 'Logical negation - reverses boolean value (opposite race condition)',
            'and': 'Logical conjunction - both conditions must be true (both tires AND engine must be good)',
            'or': 'Logical disjunction - at least one condition must be true (either DRS OR slipstream advantage)',
            'True': 'Boolean constant - represents logical truth (green flag condition)',
            'False': 'Boolean constant - represents logical false (red flag condition)',
            'None': 'Null value - represents absence of value (no data from sensor)',
            'print': 'Output function - displays text to console (radio message to pit)',
            'len': 'Length function - returns number of items in sequence (counting laps completed)',
            'range': 'Number sequence - generates sequence of numbers (lap counter)',
            'str': 'String conversion - converts value to text (converting lap time to display format)',
            'int': 'Integer conversion - converts value to whole number (converting position to integer)',
            'float': 'Decimal conversion - converts value to decimal number (precise timing measurements)',
            'list': 'List creation - creates ordered collection (race results lineup)',
            'dict': 'Dictionary creation - creates key-value pairs (driver statistics database)',
            'set': 'Set creation - creates unique value collection (unique track sectors)',
            'tuple': 'Tuple creation - creates immutable ordered collection (fixed race configuration)'
        }
    
    def explain_code(self, code: str) -> Dict[str, Any]:
        """
        Main race analysis function - provides comprehensive code telemetry
        """
        lines = code.strip().split('\n')
        
        explanation = {
            'line_by_line': self._analyze_lines(lines),
            'keywords_symbols': self._analyze_keywords_symbols(code),
            'functions_used': self._analyze_functions(code),
            'bugs_issues': self._analyze_bugs_issues(code),
            'complexity_analysis': self._analyze_complexity(code, lines),
            'inputs_outputs': self._analyze_inputs_outputs(code),
            'security_concerns': self._analyze_security(code),
            'pseudocode': self._generate_pseudocode(code),
            'summary': self._generate_summary(code)
        }
        
        return explanation
    
    def _analyze_lines(self, lines: List[str]) -> List[Dict[str, Any]]:
        """Line-by-line race track analysis"""
        analysis = []
        for i, line in enumerate(lines, 1):
            stripped_line = line.strip()
            if not stripped_line:
                continue
                
            line_analysis = {
                'line_number': i,
                'code': line,
                'explanation': self._explain_single_line(stripped_line),
                'racing_metaphor': self._get_racing_metaphor(stripped_line)
            }
            analysis.append(line_analysis)
        
        return analysis
    
    def _explain_single_line(self, line: str) -> str:
        """Detailed explanation of individual code line"""
        line = line.strip()
        
        if line.startswith('#'):
            return "📝 Comment line - provides human-readable notes about the code (like pit crew notes on car setup)"
        elif line.startswith('def '):
            return "🏗️ Function definition - creates a reusable code block that can be called multiple times (like designing a standardized pit stop procedure)"
        elif line.startswith('class '):
            return "🏎️ Class definition - creates a blueprint for objects with properties and methods (like F1 car technical specifications)"
        elif line.startswith('if '):
            return "🚦 Conditional check - executes code only if specified condition is met (like race strategy decisions based on weather)"
        elif line.startswith('for '):
            return "🔄 For loop - repeats code for each item in a collection (like analyzing each lap's performance data)"
        elif line.startswith('while '):
            return "♻️ While loop - continues executing as long as condition remains true (like racing until checkered flag appears)"
        elif line.startswith('return '):
            return "📡 Return statement - sends result back from function to caller (like telemetry sending data to mission control)"
        elif line.startswith('import ') or line.startswith('from '):
            return "📦 Import statement - includes external code libraries for additional functionality (like importing FIA racing regulations)"
        elif '=' in line and not line.startswith('='):
            return "📊 Variable assignment - stores a value in memory with a name for later use (like recording lap times in race database)"
        elif line.startswith('print('):
            return "📢 Output statement - displays information to the user (like race commentary announcing positions)"
        else:
            return "⚙️ Code execution line - performs specific operation as part of the program flow (like executing race strategy)"
    
    def _get_racing_metaphor(self, line: str) -> str:
        """Generate F1 racing metaphors for code lines"""
        if 'def ' in line:
            return "🏁 Setting up a new racing procedure"
        elif 'if ' in line:
            return "🚦 Race control decision point"
        elif 'for ' in line:
            return "🏎️ Starting lap sequence"
        elif 'print(' in line:
            return "📻 Pit radio transmission"
        elif '=' in line:
            return "📊 Recording telemetry data"
        else:
            return "⚡ High-speed execution"
    
    def _analyze_keywords_symbols(self, code: str) -> Dict[str, str]:
        """Analyze all keywords and symbols like a technical scrutineer"""
        found_items = {}
        
        # Find keywords
        for keyword, definition in self.keywords.items():
            if re.search(r'\b' + re.escape(keyword) + r'\b', code):
                found_items[keyword] = definition
        
        # Analyze symbols
        symbols = {
            '+': 'Addition operator - combines two values (like adding lap times together)',
            '-': 'Subtraction operator - finds difference between values (calculating time gap between drivers)',
            '*': 'Multiplication operator - multiplies values (calculating total race distance)',
            '/': 'Division operator - divides values (calculating average speed)',
            '//': 'Floor division - divides and rounds down to integer (complete laps finished)',
            '%': 'Modulo operator - returns remainder of division (sectors completed in current lap)',
            '**': 'Exponentiation - raises number to power (calculating exponential tire degradation)',
            '==': 'Equality comparison - checks if values are equal (checking if positions are tied)',
            '!=': 'Not equal comparison - checks if values are different (different tire strategies)',
            '<': 'Less than comparison - checks if first value is smaller (behind in race position)',
            '>': 'Greater than comparison - checks if first value is larger (ahead in race position)',
            '<=': 'Less or equal comparison - position is same or behind (not gaining positions)',
            '>=': 'Greater or equal comparison - position is same or ahead (maintaining or gaining)',
            '=': 'Assignment operator - stores value in variable (recording race data)',
            '+=': 'Addition assignment - adds value to existing variable (accumulating penalty points)',
            '-=': 'Subtraction assignment - subtracts from existing variable (losing championship points)',
            '*=': 'Multiplication assignment - multiplies existing variable (doubling points for sprint race)',
            '/=': 'Division assignment - divides existing variable (splitting points between teammates)',
            '()': 'Function call parentheses - executes function with parameters (pit crew radio call)',
            '[]': 'List/dictionary access - retrieves item at index/key (accessing driver stats)',
            '{}': 'Dictionary/set literal - creates key-value pairs or unique collection (team roster)',
            ':': 'Dictionary separator or code block indicator - defines relationships (driver:team mapping)',
            ';': 'Statement separator - ends statement (rarely used in Python, like race sector timing)',
            ',': 'Item separator - separates parameters or list items (separating lap times)',
            '.': 'Attribute access - accesses object properties or methods (car.engine.temperature)',
            '&': 'Bitwise AND - performs binary AND operation (technical sensor data processing)',
            '|': 'Bitwise OR - performs binary OR operation (combining telemetry signals)',
            '^': 'Bitwise XOR - performs exclusive OR operation (comparing different data sources)',
            '~': 'Bitwise NOT - performs binary complement (inverting sensor readings)',
            '<<': 'Left bit shift - shifts bits left (advanced data encoding for telemetry)',
            '>>': 'Right bit shift - shifts bits right (decoding compressed race data)'
        }
        
        for symbol, definition in symbols.items():
            if symbol in code:
                found_items[f"'{symbol}'"] = definition
        
        return found_items
    
    def _analyze_functions(self, code: str) -> Dict[str, Dict[str, str]]:
        """Analyze functions like a race engineer analyzing car performance"""
        functions = {}
        
        # Built-in functions detection
        builtin_functions = {
            'print': {
                'role': 'Display output to console',
                'definition': 'Built-in function that outputs text or variables to the screen (like race commentary)',
                'usage': 'Communication and debugging tool for developers'
            },
            'len': {
                'role': 'Calculate sequence length',
                'definition': 'Returns the number of items in a sequence like list, string, or tuple (counting laps)',
                'usage': 'Determining size of data collections for processing'
            },
            'range': {
                'role': 'Generate number sequences',
                'definition': 'Creates a sequence of numbers for iteration (like lap counter from 1 to 70)',
                'usage': 'Controlling loop iterations and creating numeric sequences'
            },
            'input': {
                'role': 'Receive user input',
                'definition': 'Pauses program to receive text input from user (like driver radio messages)',
                'usage': 'Interactive programs that need user participation'
            },
            'str': {
                'role': 'Convert to string',
                'definition': 'Converts any data type to text format (converting lap time to displayable text)',
                'usage': 'Data type conversion for display and text processing'
            },
            'int': {
                'role': 'Convert to integer',
                'definition': 'Converts values to whole numbers (converting position string to number)',
                'usage': 'Mathematical operations requiring whole numbers'
            },
            'float': {
                'role': 'Convert to decimal',
                'definition': 'Converts values to decimal numbers (precise timing measurements)',
                'usage': 'Precise calculations requiring decimal precision'
            },
            'list': {
                'role': 'Create ordered collection',
                'definition': 'Creates a mutable sequence of items (race results that can be updated)',
                'usage': 'Storing and manipulating ordered data collections'
            },
            'dict': {
                'role': 'Create key-value mapping',
                'definition': 'Creates a collection of key-value pairs (driver statistics database)',
                'usage': 'Storing related data with meaningful identifiers'
            },
            'max': {
                'role': 'Find maximum value',
                'definition': 'Returns the largest value from a sequence (fastest lap time)',
                'usage': 'Finding optimal or extreme values in data sets'
            },
            'min': {
                'role': 'Find minimum value',
                'definition': 'Returns the smallest value from a sequence (shortest pit stop time)',
                'usage': 'Finding optimal or minimum values in data sets'
            },
            'sum': {
                'role': 'Calculate total',
                'definition': 'Adds all numbers in a sequence (total championship points)',
                'usage': 'Mathematical aggregation of numeric data'
            },
            'abs': {
                'role': 'Absolute value',
                'definition': 'Returns positive version of number (time difference magnitude)',
                'usage': 'Distance and magnitude calculations'
            },
            'round': {
                'role': 'Round numbers',
                'definition': 'Rounds decimal numbers to specified precision (rounding lap times)',
                'usage': 'Formatting numbers for display and reducing precision'
            }
        }
        
        # Find built-in functions in code
        for func_name, func_info in builtin_functions.items():
            if re.search(r'\b' + func_name + r'\s*\(', code):
                functions[func_name] = func_info
        
        # Find custom function definitions
        func_pattern = r'def\s+(\w+)\s*\([^)]*\):'
        custom_functions = re.findall(func_pattern, code)
        
        for func_name in custom_functions:
            functions[func_name] = {
                'role': 'Custom function defined in this code',
                'definition': f'User-defined function that encapsulates specific logic (custom race strategy: {func_name})',
                'usage': 'Modular code organization and reusability'
            }
        
        return functions
    
    def _analyze_bugs_issues(self, code: str) -> List[Dict[str, str]]:
        """Technical inspection for potential issues"""
        issues = []
        lines = code.split('\n')
        
        # Check for common issues
        for i, line in enumerate(lines, 1):
            stripped_line = line.strip()
            
            # Indentation issues
            if line and not line.startswith(' ') and not line.startswith('\t') and i > 1:
                if any(lines[j].strip().startswith(('if ', 'for ', 'while ', 'def ', 'class ')) for j in range(max(0, i-3), i)):
                    if not stripped_line.startswith(('#', 'else:', 'elif ', 'except:', 'finally:')):
                        issues.append({
                            'type': '🚨 Potential Indentation Issue',
                            'line': i,
                            'description': f'Line {i} may need proper indentation (like F1 car not following racing line)',
                            'suggestion': 'Ensure proper indentation for code blocks'
                        })
            
            # Undefined variables (basic check)
            if '=' not in stripped_line and 'def ' not in stripped_line and 'class ' not in stripped_line:
                variables = re.findall(r'\b([a-zA-Z_]\w*)\b', stripped_line)
                for var in variables:
                    if var not in ['print', 'len', 'range', 'str', 'int', 'float', 'True', 'False', 'None']:
                        # This is a simplified check - in real implementation, you'd need proper AST analysis
                        pass
            
            # Missing colons
            if re.match(r'^\s*(if|elif|else|for|while|def|class|try|except|finally|with)\b', stripped_line):
                if not stripped_line.rstrip().endswith(':'):
                    issues.append({
                        'type': '🚨 Syntax Error',
                        'line': i,
                        'description': f'Line {i} is missing a colon (like missing chequered flag at race end)',
                        'suggestion': 'Add colon (:) at the end of the statement'
                    })
        
        # If no issues found
        if not issues:
            issues.append({
                'type': '✅ Clean Race',
                'line': 'All',
                'description': 'No obvious issues detected - code looks race-ready!',
                'suggestion': 'Code appears to follow proper syntax (like a perfectly executed qualifying lap)'
            })
        
        return issues
    
    def _analyze_complexity(self, code: str, lines: List[str]) -> Dict[str, Any]:
        """Performance analysis like F1 car telemetry"""
        analysis = {
            'time_complexity': 'O(1) - Constant time (pit stop speed)',
            'space_complexity': 'O(1) - Constant space (minimal memory usage)',
            'code_metrics': {
                'total_lines': len(lines),
                'code_lines': len([l for l in lines if l.strip() and not l.strip().startswith('#')]),
                'comment_lines': len([l for l in lines if l.strip().startswith('#')]),
                'blank_lines': len([l for l in lines if not l.strip()])
            },
            'complexity_factors': []
        }
        
        # Detect loops (increase complexity)
        loop_count = len(re.findall(r'\b(for|while)\b', code))
        if loop_count > 0:
            analysis['time_complexity'] = f'O(n) - Linear time due to {loop_count} loop(s) (like completing all race laps)'
            analysis['complexity_factors'].append(f'{loop_count} loop(s) detected - increases execution time')
        
        # Nested loops
        nested_loops = 0
        for line in lines:
            if re.search(r'^\s+\s+.*(for|while)\b', line):  # Rough detection of nested loops
                nested_loops += 1
        
        if nested_loops > 0:
            analysis['time_complexity'] = 'O(n²) - Quadratic time (nested loops like qualifying sessions within race weekends)'
            analysis['complexity_factors'].append(f'Nested loops detected - significantly increases computation time')
        
        # Function definitions
        func_count = len(re.findall(r'\bdef\s+\w+', code))
        if func_count > 0:
            analysis['complexity_factors'].append(f'{func_count} function(s) defined - good modular design (like specialized F1 departments)')
        
        return analysis
    
    def _analyze_inputs_outputs(self, code: str) -> Dict[str, List[str]]:
        """Data flow analysis like race telemetry streams"""
        analysis = {
            'inputs': [],
            'outputs': [],
            'data_flow': 'Internal processing (like onboard computer calculations)'
        }
        
        # Detect inputs
        if 'input(' in code:
            analysis['inputs'].append('User keyboard input (driver radio messages)')
        
        # Function parameters
        param_matches = re.findall(r'def\s+\w+\s*\(([^)]+)\)', code)
        for params in param_matches:
            if params.strip():
                analysis['inputs'].append(f'Function parameters: {params.strip()} (pit crew instructions)')
        
        # Detect outputs
        if 'print(' in code:
            analysis['outputs'].append('Console text output (race commentary)')
        
        if 'return ' in code:
            analysis['outputs'].append('Function return values (telemetry data to mission control)')
        
        # File operations (if any)
        if any(op in code for op in ['open(', 'write(', 'read(']):
            analysis['inputs'].append('File system operations (race data logging)')
            analysis['outputs'].append('File system operations (saving race results)')
        
        return analysis
    
    def _analyze_security(self, code: str) -> List[Dict[str, str]]:
        """Security analysis like F1 technical regulations compliance"""
        concerns = []
        
        # Check for potentially dangerous functions
        dangerous_functions = ['eval', 'exec', 'input', '__import__']
        for func in dangerous_functions:
            if func in code:
                if func == 'eval':
                    concerns.append({
                        'level': '🚨 High Risk',
                        'issue': 'eval() function detected',
                        'description': 'Can execute arbitrary code - like allowing unauthorized modifications to F1 car during race',
                        'recommendation': 'Use safer alternatives like ast.literal_eval() for data parsing'
                    })
                elif func == 'exec':
                    concerns.append({
                        'level': '🚨 High Risk', 
                        'issue': 'exec() function detected',
                        'description': 'Can execute arbitrary Python code - major security risk',
                        'recommendation': 'Avoid exec() or implement strict input validation'
                    })
                elif func == 'input':
                    concerns.append({
                        'level': '⚠️ Medium Risk',
                        'issue': 'input() function detected',
                        'description': 'User input can be unpredictable - like unexpected weather during race',
                        'recommendation': 'Validate and sanitize all user inputs'
                    })
        
        # Check for file operations
        if any(op in code for op in ['open(', 'file(', 'read(', 'write(']):
            concerns.append({
                'level': '⚠️ Medium Risk',
                'issue': 'File operations detected',
                'description': 'File access can pose security risks - like unauthorized access to race data',
                'recommendation': 'Ensure proper file permissions and input validation'
            })
        
        if not concerns:
            concerns.append({
                'level': '✅ All Clear',
                'issue': 'No obvious security concerns',
                'description': 'Code appears to follow safe practices (like passing F1 technical inspection)',
                'recommendation': 'Continue following secure coding practices'
            })
        
        return concerns
    
    def _generate_pseudocode(self, code: str) -> List[str]:
        """Generate race strategy pseudocode"""
        lines = [line.strip() for line in code.split('\n') if line.strip() and not line.strip().startswith('#')]
        pseudocode = ['🏁 Race Strategy Breakdown:']
        
        for i, line in enumerate(lines, 1):
            if line.startswith('def '):
                func_name = re.search(r'def\s+(\w+)', line)
                if func_name:
                    pseudocode.append(f'{i}. START racing procedure: {func_name.group(1)}')
            elif line.startswith('if '):
                pseudocode.append(f'{i}. DECISION POINT: Check race conditions')
            elif line.startswith('else:'):
                pseudocode.append(f'{i}. ALTERNATIVE: Execute backup strategy')
            elif line.startswith('elif '):
                pseudocode.append(f'{i}. ADDITIONAL CHECK: Alternative race condition')
            elif line.startswith('for '):
                pseudocode.append(f'{i}. REPEAT: Execute for each lap/iteration')
            elif line.startswith('while '):
                pseudocode.append(f'{i}. CONTINUE: Keep racing until condition changes')
            elif 'print(' in line:
                pseudocode.append(f'{i}. ANNOUNCE: Broadcast race information')
            elif line.startswith('return '):
                pseudocode.append(f'{i}. FINISH: Send results to race control')
            elif '=' in line and not line.startswith('='):
                pseudocode.append(f'{i}. RECORD: Store race data')
            else:
                pseudocode.append(f'{i}. EXECUTE: Perform race operation')
        
        pseudocode.append('🏆 END of race strategy')
        return pseudocode
    
    def _generate_summary(self, code: str) -> Dict[str, str]:
        """Generate intelligent summary like F1 race report"""
        lines = [line.strip() for line in code.split('\n') if line.strip() and not line.strip().startswith('#')]
        
        # Analyze code structure
        has_functions = bool(re.search(r'\bdef\s+\w+', code))
        has_loops = bool(re.search(r'\b(for|while)\b', code))
        has_conditionals = bool(re.search(r'\b(if|elif)\b', code))
        has_input = 'input(' in code
        has_output = 'print(' in code
        
        # Generate summary based on analysis
        what_it_does = "This code "
        if has_functions:
            what_it_does += "defines custom functions for modular code organization, "
        if has_loops:
            what_it_does += "uses loops to repeat operations efficiently, "
        if has_conditionals:
            what_it_does += "makes decisions based on different conditions, "
        if has_input:
            what_it_does += "interacts with users through input collection, "
        if has_output:
            what_it_does += "provides output through console display, "
        
        what_it_does = what_it_does.rstrip(', ') + "."
        
        why_useful = "🎯 Purpose: "
        if has_functions and has_loops:
            why_useful += "This code demonstrates advanced programming concepts with reusable functions and efficient iteration - like a complete F1 race strategy system."
        elif has_functions:
            why_useful += "Modular design makes code maintainable and reusable - like standardized F1 pit procedures."
        elif has_loops:
            why_useful += "Efficient repetitive processing - like automated lap time analysis."
        elif has_conditionals:
            why_useful += "Smart decision-making capabilities - like adaptive race strategies."
        else:
            why_useful += "Demonstrates basic programming fundamentals - like learning F1 racing basics."
        
        when_to_use = "⚡ Best Used When: "
        if has_input and has_output:
            when_to_use += "Building interactive applications that need user engagement and feedback."
        elif has_functions:
            when_to_use += "Creating reusable code libraries or complex applications requiring modular design."
        elif has_loops:
            when_to_use += "Processing large datasets or performing repetitive calculations efficiently."
        else:
            when_to_use += "Learning programming fundamentals or creating simple automation scripts."
        
        return {
            'what_it_does': what_it_does,
            'why_useful': why_useful,
            'when_to_use': when_to_use,
            'racing_verdict': f"🏁 Race Performance: Code complexity level {'High' if has_functions and has_loops else 'Medium' if has_functions or has_loops else 'Beginner'} - {'Championship-ready' if len(lines) > 10 else 'Practice session quality'}"
        }