web_development_quiz = {
    "course_code": "ATU 203",
    "course_name": "Web Development",
    "total_questions": 50,
    "questions": [
        
    
    {
        "id": 1,
        "type": "multiple_choice",
        "question": "A government portal must support screen readers and assistive technologies. Which HTML choice best fulfills this requirement?",
        "options": [
            "Non-semantic containers",
            "Semantic structural elements",
            "Inline styling",
            "Image-based navigation"
        ],
        "correct_answer": 1,
        "explanation": "Semantic HTML elements (like <header>, <nav>, <main>, <article>) provide meaning to screen readers and assistive technologies, improving accessibility."
    },
    {
        "id": 2,
        "type": "multiple_choice",
        "question": "A developer notices inconsistent rendering across browsers. Which HTML-related issue is MOST likely the cause?",
        "options": [
            "Incorrect semantic tags",
            "Improper tag nesting",
            "External CSS usage",
            "JavaScript execution order"
        ],
        "correct_answer": 1,
        "explanation": "Improperly nested HTML tags can cause browsers to interpret the structure differently, leading to inconsistent rendering across browsers."
    },
    {
        "id": 3,
        "type": "multiple_choice",
        "question": "Which CSS box model issue MOST commonly causes layout inconsistency?",
        "options": [
            "Missing fonts",
            "Incorrect box-sizing",
            "Wrong selectors",
            "JavaScript conflicts"
        ],
        "correct_answer": 1,
        "explanation": "The box-sizing property determines how element dimensions are calculated. Inconsistent box-sizing values can cause unexpected layout differences."
    },
    {
        "id": 4,
        "type": "multiple_choice",
        "question": "Which CSS approach best supports future UI redesign without changing HTML?",
        "options": [
            "Inline styles",
            "External modular CSS",
            "Embedded styles",
            "Table-based layouts"
        ],
        "correct_answer": 1,
        "explanation": "External modular CSS separates presentation from content, allowing complete redesigns by swapping or modifying CSS files without touching HTML structure."
    },
    {
        "id": 5,
        "type": "multiple_choice",
        "question": "Excessive DOM manipulation leads to:",
        "options": [
            "Faster rendering",
            "Performance degradation",
            "Improved accessibility",
            "Smaller files"
        ],
        "correct_answer": 1,
        "explanation": "Frequent or excessive DOM manipulations force the browser to recalculate layouts and repaint elements, causing performance degradation."
    },
    {
        "id": 6,
        "type": "multiple_choice",
        "question": "A page freezes due to heavy JavaScript execution. Which optimization best resolves this?",
        "options": [
            "Inline scripts",
            "Event delegation",
            "Blocking scripts",
            "Embedded CSS"
        ],
        "correct_answer": 1,
        "explanation": "Event delegation reduces the number of event listeners by attaching a single listener to a parent element, improving performance with fewer DOM operations."
    },
    {
        "id": 7,
        "type": "multiple_choice",
        "question": "Why is PHP input validation critical even when JavaScript validation exists?",
        "options": [
            "JavaScript is faster",
            "Users can bypass client-side checks",
            "PHP improves UI",
            "HTML prevents errors"
        ],
        "correct_answer": 1,
        "explanation": "Client-side validation can be bypassed by disabling JavaScript or manipulating the browser. Server-side validation in PHP is the final security barrier."
    },
    {
        "id": 8,
        "type": "multiple_choice",
        "question": "A site is difficult to debug. Which design flaw is MOST likely?",
        "options": [
            "External files",
            "Mixed responsibilities across layers",
            "Semantic HTML",
            "Modular CSS"
        ],
        "correct_answer": 1,
        "explanation": "When HTML, CSS, and JavaScript responsibilities are mixed together, it becomes difficult to isolate and fix bugs in specific layers."
    },
    {
        "id": 9,
        "type": "multiple_choice",
        "question": "Which technology combination best supports dynamic form processing?",
        "options": [
            "HTML + CSS",
            "HTML + JavaScript + PHP",
            "CSS + PHP",
            "JavaScript only"
        ],
        "correct_answer": 1,
        "explanation": "HTML provides structure, JavaScript handles client-side interaction, and PHP processes data server-side—a complete stack for dynamic forms."
    },
    {
        "id": 10,
        "type": "multiple_choice",
        "question": "A web application must adapt to future technologies. Which principle best supports this?",
        "options": [
            "Rigid design",
            "Standards-compliant development",
            "Inline CSS",
            "Table layouts"
        ],
        "correct_answer": 1,
        "explanation": "Following W3C web standards ensures compatibility with current and future browsers and devices, making applications more adaptable."
    },
    {
        "id": 11,
        "type": "multiple_choice",
        "question": "Which decision MOST improves cross-browser compatibility?",
        "options": [
            "Inline CSS",
            "W3C-compliant standards",
            "JavaScript-only UI",
            "Fixed layouts"
        ],
        "correct_answer": 1,
        "explanation": "W3C standards ensure consistent interpretation of code across different browsers, reducing compatibility issues."
    },
    {
        "id": 12,
        "type": "multiple_choice",
        "question": "A form accepts invalid data despite client checks. Which improvement is required?",
        "options": [
            "Better CSS",
            "Stronger server-side validation",
            "Inline scripts",
            "HTML comments"
        ],
        "correct_answer": 1,
        "explanation": "Client-side validation is easily bypassed. Server-side validation is essential for data integrity and security."
    },
    {
        "id": 13,
        "type": "multiple_choice",
        "question": "A website redesign requires minimal HTML changes. Which prior decision enabled this?",
        "options": [
            "Inline styles",
            "External CSS usage",
            "Hard-coded JavaScript",
            "Embedded PHP"
        ],
        "correct_answer": 1,
        "explanation": "External CSS separates presentation from content, allowing visual redesigns without altering HTML structure."
    },
    {
        "id": 14,
        "type": "multiple_choice",
        "question": "Which design principle BEST supports collaborative development?",
        "options": [
            "Individual coding styles",
            "Standardized structure",
            "Inline scripting",
            "Table layouts"
        ],
        "correct_answer": 1,
        "explanation": "Standardized code structure and conventions enable multiple developers to work together efficiently and understand each other's code."
    },
    {
        "id": 15,
        "type": "multiple_choice",
        "question": "Which approach ensures adaptability to new devices?",
        "options": [
            "Fixed layouts",
            "Responsive design",
            "Absolute positioning",
            "Inline CSS"
        ],
        "correct_answer": 1,
        "explanation": "Responsive design uses flexible layouts and media queries to adapt content to any screen size or device."
    },
    {
        "id": 16,
        "type": "multiple_choice",
        "question": "Which design flaw MOST affects accessibility?",
        "options": [
            "Missing JavaScript",
            "Non-semantic HTML",
            "External CSS",
            "PHP includes"
        ],
        "correct_answer": 1,
        "explanation": "Non-semantic HTML (like excessive <div> tags) provides no structural meaning to assistive technologies, severely impacting accessibility."
    },
    {
        "id": 17,
        "type": "multiple_choice",
        "question": "Why should frontend and backend be loosely coupled?",
        "options": [
            "To slow execution",
            "To allow independent evolution",
            "To reduce security",
            "To simplify CSS"
        ],
        "correct_answer": 1,
        "explanation": "Loose coupling allows frontend and backend to be developed, updated, and maintained independently without breaking each other."
    },
    {
        "id": 18,
        "type": "multiple_choice",
        "question": "Which layer MOST affects data integrity?",
        "options": [
            "CSS",
            "Backend processing",
            "HTML semantics",
            "JavaScript events"
        ],
        "correct_answer": 1,
        "explanation": "Backend processing handles validation, sanitization, and database operations that ensure data remains accurate and consistent."
    },
    {
        "id": 19,
        "type": "multiple_choice",
        "question": "Why should web development follow W3C standards?",
        "options": [
            "To limit creativity",
            "To ensure interoperability",
            "To improve branding",
            "To reduce hosting cost"
        ],
        "correct_answer": 1,
        "explanation": "W3C standards ensure websites work consistently across different browsers, devices, and platforms."
    },
    {
        "id": 20,
        "type": "multiple_choice",
        "question": "Which web layer MOST affects scalability?",
        "options": [
            "CSS",
            "Backend processing",
            "HTML semantics",
            "Images"
        ],
        "correct_answer": 1,
        "explanation": "Backend architecture, including server logic and database design, determines how well a system handles increased load and users."
    },
    {
        "id": 21,
        "type": "multiple_choice",
        "question": "A table displaying students' results becomes difficult to read on small screens. Which design decision BEST improves usability without removing the table?",
        "options": [
            "Converting the table into images",
            "Adding CSS for responsive table styling",
            "Removing table headers",
            "Using inline styles only"
        ],
        "correct_answer": 1,
        "explanation": "Responsive CSS techniques (like horizontal scrolling or reformatting) can make tables usable on small screens while preserving data structure."
    },
    {
        "id": 22,
        "type": "multiple_choice",
        "question": "Why is the <th> element preferred over <td> for table headings?",
        "options": [
            "It reduces file size",
            "It improves accessibility and semantics",
            "It applies automatic borders",
            "It increases table speed"
        ],
        "correct_answer": 1,
        "explanation": "<th> semantically identifies header cells, helping screen readers understand table structure and improving accessibility."
    },
    {
        "id": 23,
        "type": "multiple_choice",
        "question": "A developer forgets to include <thead> and <tbody> in a large table. What is the MOST likely consequence?",
        "options": [
            "The table will not display",
            "Reduced structure and accessibility",
            "JavaScript will fail",
            "CSS cannot be applied"
        ],
        "correct_answer": 1,
        "explanation": "While the table still displays, missing these structural elements reduces semantic meaning and can complicate styling and accessibility."
    },
    {
        "id": 24,
        "type": "multiple_choice",
        "question": "Which scenario BEST justifies the use of an HTML table?",
        "options": [
            "Page layout design",
            "Navigation menus",
            "Displaying structured tabular data",
            "Image galleries"
        ],
        "correct_answer": 2,
        "explanation": "Tables are specifically designed for displaying data that naturally fits in rows and columns, not for layout or navigation."
    },
    {
        "id": 25,
        "type": "multiple_choice",
        "question": "Why are tables discouraged for page layout in modern web development?",
        "options": [
            "They increase accessibility",
            "They limit responsiveness and flexibility",
            "They load faster",
            "They improve SEO"
        ],
        "correct_answer": 1,
        "explanation": "Table-based layouts are rigid, difficult to make responsive, and mix presentation with content, violating modern web design principles."
    },
    {
        "id": 26,
        "type": "multiple_choice",
        "question": "Which table attribute BEST improves readability by grouping related rows?",
        "options": [
            "border",
            "cellpadding",
            "rowspan",
            "<tbody>"
        ],
        "correct_answer": 3,
        "explanation": "<tbody> groups rows into logical sections, improving both visual organization and semantic structure of tables."
    },
    {
        "id": 27,
        "type": "multiple_choice",
        "question": "A table header should be associated with its data cells to improve accessibility. Which attribute supports this?",
        "options": [
            "class",
            "headers",
            "id",
            "style"
        ],
        "correct_answer": 1,
        "explanation": "The headers attribute associates data cells with their corresponding header cells by referencing header IDs, crucial for screen readers."
    },
    {
        "id": 28,
        "type": "multiple_choice",
        "question": "When a table cell spans multiple columns, which attribute is used?",
        "options": [
            "rowspan",
            "colspan",
            "merge",
            "span"
        ],
        "correct_answer": 1,
        "explanation": "colspan specifies how many columns a cell should occupy, useful for merging cells horizontally."
    },
    {
        "id": 29,
        "type": "multiple_choice",
        "question": "Which practice MOST improves the accessibility of large data tables?",
        "options": [
            "Using colors only",
            "Adding captions and headers",
            "Increasing font size only",
            "Removing borders"
        ],
        "correct_answer": 1,
        "explanation": "Captions describe table purpose while headers provide structure—both are essential for screen reader users navigating large tables."
    },
    {
        "id": 30,
        "type": "multiple_choice",
        "question": "A table needs a title describing its content. Which element is MOST appropriate?",
        "options": [
            "<title>",
            "<caption>",
            "<thead>",
            "<summary>"
        ],
        "correct_answer": 1,
        "explanation": "<caption> provides a title or description specifically for tables, appearing directly with the table content."
    },
    {
        "id": 31,
        "type": "multiple_choice",
        "question": "A student builds a login page where PHP processes the credentials before sending the page back to the browser. This means PHP scripts are executed on the server before the page is sent to the browser.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "PHP is server-side, meaning it executes on the server and only the resulting HTML is sent to the browser."
    },
    {
        "id": 32,
        "type": "multiple_choice",
        "question": "During testing, a developer views the page source in the browser and cannot see any PHP code. This indicates that PHP code is hidden from users after server execution.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "PHP executes on the server, so users only see the HTML output, never the underlying PHP code."
    },
    {
        "id": 33,
        "type": "multiple_choice",
        "question": "A student uses CSS to change text color, font size, and page layout without modifying the HTML structure. This shows that CSS controls the presentation of web pages.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "CSS is specifically designed to handle presentation, separating visual styling from HTML content structure."
    },
    {
        "id": 34,
        "type": "multiple_choice",
        "question": "A developer styles a large website using inline CSS on every HTML element. This approach improves long-term maintainability.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 1,
        "explanation": "Inline CSS mixes presentation with content, making sites extremely difficult to maintain and update consistently."
    },
    {
        "id": 35,
        "type": "multiple_choice",
        "question": "A developer assumes JavaScript code runs on the web server before the page is sent to the browser. This assumption is correct.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 1,
        "explanation": "JavaScript is client-side and runs in the browser after the page is received, not on the server before sending."
    },
    {
        "id": 36,
        "type": "multiple_choice",
        "question": "The CSS property used to change the background color of an element is:",
        "options": [
            "color",
            "background-color",
            "bgcolor",
            "background"
        ],
        "correct_answer": 1,
        "explanation": "background-color is the standard CSS property for setting an element's background color."
    },
    {
        "id": 37,
        "type": "multiple_choice",
        "question": "The HTML element used to create a table row is:",
        "options": [
            "<tr>",
            "<td>",
            "<th>",
            "<row>"
        ],
        "correct_answer": 0,
        "explanation": "<tr> (table row) defines a row of cells in an HTML table."
    },
    {
        "id": 38,
        "type": "multiple_choice",
        "question": "The HTML attribute that specifies the destination of a hyperlink is:",
        "options": [
            "src",
            "link",
            "href",
            "url"
        ],
        "correct_answer": 2,
        "explanation": "The href attribute in an <a> tag specifies the URL or destination of the hyperlink."
    },
    {
        "id": 39,
        "type": "multiple_choice",
        "question": "The PHP function used to start a session is:",
        "options": [
            "session_open()",
            "session_start()",
            "begin_session()",
            "init_session()"
        ],
        "correct_answer": 1,
        "explanation": "session_start() initializes a new or resumes an existing PHP session for maintaining user state across pages."
    },
    {
        "id": 40,
        "type": "multiple_choice",
        "question": "A website that adjusts automatically to different screen sizes is described as:",
        "options": [
            "Adaptive",
            "Responsive",
            "Flexible",
            "Dynamic"
        ],
        "correct_answer": 1,
        "explanation": "Responsive web design uses fluid grids and media queries to automatically adapt layouts to different screen sizes."
    },
    {
        "id": 41,
        "type": "multiple_choice",
        "question": "A university website is failing accessibility audits and ranking poorly on search engines. Which HTML redesign decision would MOST effectively address both issues?",
        "options": [
            "Replacing <div> tags with semantic elements",
            "Increasing font sizes using inline styles",
            "Embedding JavaScript inside HTML",
            "Using tables for page layout"
        ],
        "correct_answer": 0,
        "explanation": "Semantic HTML improves both accessibility (screen readers understand structure) and SEO (search engines better interpret content)."
    },
    {
        "id": 42,
        "type": "multiple_choice",
        "question": "A large web project involves multiple developers. Which HTML practice best supports collaboration and long-term maintenance?",
        "options": [
            "Using deeply nested <div> elements",
            "Writing inline HTML styles",
            "Applying semantic HTML structure",
            "Embedding PHP directly in HTML"
        ],
        "correct_answer": 2,
        "explanation": "Semantic HTML creates clear, self-documenting structure that all developers can understand and maintain consistently."
    },
    {
        "id": 43,
        "type": "multiple_choice",
        "question": "A multilingual website struggles with search indexing. Which HTML attribute strategy best resolves this?",
        "options": [
            "lang attribute usage",
            "id attribute consistency",
            "class naming",
            "Inline metadata"
        ],
        "correct_answer": 0,
        "explanation": "The lang attribute tells search engines and browsers which language content is in, improving international SEO and accessibility."
    },
    {
        "id": 44,
        "type": "multiple_choice",
        "question": "A website breaks on tablets but works on desktops. Which CSS strategy best fixes this issue?",
        "options": [
            "Fixed widths",
            "Media queries",
            "Inline styling",
            "Absolute positioning"
        ],
        "correct_answer": 1,
        "explanation": "Media queries apply different styles based on device characteristics like screen width, enabling responsive design."
    },
    {
        "id": 45,
        "type": "multiple_choice",
        "question": "Why is Flexbox preferred over floats for modern layouts?",
        "options": [
            "Floats load faster",
            "Flexbox handles alignment dynamically",
            "Floats support responsiveness better",
            "Flexbox removes the need for HTML"
        ],
        "correct_answer": 1,
        "explanation": "Flexbox provides powerful alignment, distribution, and dynamic sizing capabilities that floats cannot easily achieve."
    },
    {
        "id": 46,
        "type": "multiple_choice",
        "question": "Absolute positioning negatively impacts responsiveness because it:",
        "options": [
            "Ignores screen size changes",
            "Breaks JavaScript",
            "Disables HTML semantics",
            "Removes accessibility"
        ],
        "correct_answer": 0,
        "explanation": "Absolutely positioned elements are removed from normal document flow and don't adapt well to different screen sizes."
    },
    {
        "id": 47,
        "type": "multiple_choice",
        "question": "A form submits invalid data repeatedly. Which JavaScript strategy best prevents this?",
        "options": [
            "Server-side validation only",
            "Client-side validation before submission",
            "Removing form constraints",
            "Using CSS validation"
        ],
        "correct_answer": 1,
        "explanation": "Client-side validation provides immediate feedback to users before submission, preventing invalid data from being sent unnecessarily."
    },
    {
        "id": 48,
        "type": "multiple_choice",
        "question": "Why is event-driven programming essential in modern web apps?",
        "options": [
            "It reduces HTML size",
            "It responds dynamically to user actions",
            "It replaces CSS",
            "It improves database speed"
        ],
        "correct_answer": 1,
        "explanation": "Event-driven programming allows web apps to react to user interactions (clicks, typing, etc.) in real-time, creating dynamic experiences."
    },
    {
        "id": 49,
        "type": "multiple_choice",
        "question": "Why is PHP classified as server-side scripting?",
        "options": [
            "It runs in the browser",
            "It executes before content reaches the client",
            "It styles pages",
            "It handles CSS"
        ],
        "correct_answer": 1,
        "explanation": "PHP executes on the web server, generating HTML that is then sent to the client's browser."
    },
    {
        "id": 50,
        "type": "multiple_choice",
        "question": "A login system works locally but fails online. Which PHP issue is MOST likely?",
        "options": [
            "HTML validation",
            "Server configuration",
            "CSS conflicts",
            "JavaScript errors"
        ],
        "correct_answer": 1,
        "explanation": "Server configuration differences (PHP version, extensions, settings) between local and production environments often cause failures."
    },
    {
        "id": 51,
        "type": "multiple_choice",
        "question": "Why should PHP files not expose logic to users?",
        "options": [
            "PHP runs client-side",
            "PHP executes before response",
            "PHP improves accessibility",
            "PHP handles CSS"
        ],
        "correct_answer": 1,
        "explanation": "PHP executes on the server, so only its output (HTML) is sent—users never see the actual PHP code logic."
    },
    {
        "id": 52,
        "type": "multiple_choice",
        "question": "A dynamic website fails when JavaScript is disabled. Which design principle was ignored?",
        "options": [
            "Graceful degradation",
            "Inline styling",
            "Server caching",
            "Fixed layout"
        ],
        "correct_answer": 0,
        "explanation": "Graceful degradation ensures core functionality remains available even when advanced features (like JavaScript) are disabled."
    },
    {
        "id": 53,
        "type": "multiple_choice",
        "question": "Why is separation of concerns important in web development?",
        "options": [
            "It reduces browser compatibility",
            "It improves maintainability and scalability",
            "It increases page size",
            "It limits functionality"
        ],
        "correct_answer": 1,
        "explanation": "Separating HTML (structure), CSS (presentation), and JavaScript (behavior) makes code more organized, maintainable, and scalable."
    },
    {
        "id": 54,
        "type": "multiple_choice",
        "question": "A university portal redesign focuses on accessibility, performance, and scalability. Which combined approach best meets these goals?",
        "options": [
            "Table layouts and inline CSS",
            "Semantic HTML, external CSS, modular JS, server-side PHP",
            "JavaScript-only rendering",
            "Embedded styles and scripts"
        ],
        "correct_answer": 1,
        "explanation": "This combination addresses all goals: semantic HTML for accessibility, external CSS for performance, modular JS for maintainability, and server-side PHP for scalability."
    },
    {
        "id": 55,
        "type": "multiple_choice",
        "question": "A site works visually but fails usability testing. Which area was MOST neglected?",
        "options": [
            "Backend logic",
            "User experience and accessibility",
            "Database structure",
            "Server hosting"
        ],
        "correct_answer": 1,
        "explanation": "Visual design alone doesn't ensure usability—user experience design and accessibility considerations are crucial for real-world use."
    },
    {
        "id": 56,
        "type": "multiple_choice",
        "question": "Why is accessibility a core quality metric in web development?",
        "options": [
            "It improves aesthetics",
            "It ensures inclusivity and legal compliance",
            "It reduces server load",
            "It replaces usability"
        ],
        "correct_answer": 1,
        "explanation": "Accessibility ensures websites are usable by people with disabilities, which is both ethically important and legally required in many contexts."
    },
    {
        "id": 57,
        "type": "multiple_choice",
        "question": "Which development choice MOST improves maintainability?",
        "options": [
            "Inline styling",
            "Clear separation of technologies",
            "Embedded scripts",
            "Table layouts"
        ],
        "correct_answer": 1,
        "explanation": "Separating HTML, CSS, and JavaScript into distinct files and layers makes each part easier to understand and modify independently."
    },
    {
        "id": 58,
        "type": "multiple_choice",
        "question": "Which practice BEST ensures long-term project success?",
        "options": [
            "Rapid coding",
            "Standards-based development",
            "Hard-coded solutions",
            "Minimal documentation"
        ],
        "correct_answer": 1,
        "explanation": "Following web standards ensures compatibility, maintainability, and future-proofing as technologies evolve."
    },
    {
        "id": 59,
        "type": "multiple_choice",
        "question": "A poorly structured project MOST affects which phase?",
        "options": [
            "Deployment",
            "Maintenance",
            "Hosting",
            "Rendering"
        ],
        "correct_answer": 1,
        "explanation": "Poor structure makes maintenance difficult and costly—fixing bugs, adding features, and understanding code become time-consuming."
    },
    {
        "id": 60,
        "type": "multiple_choice",
        "question": "Which technology combination BEST supports interactive, secure websites?",
        "options": [
            "HTML + CSS",
            "HTML + CSS + JavaScript + PHP",
            "CSS + PHP",
            "JavaScript only"
        ],
        "correct_answer": 1,
        "explanation": "This full stack provides structure (HTML), presentation (CSS), client-side interaction (JavaScript), and server-side security/processing (PHP)."
    },
    {
        "id": 61,
        "type": "multiple_choice",
        "question": "A website fails compliance audits. Which aspect was MOST likely ignored?",
        "options": [
            "Color schemes",
            "Accessibility standards",
            "Image resolution",
            "Fonts"
        ],
        "correct_answer": 1,
        "explanation": "Accessibility standards (like WCAG) are common compliance requirements that are frequently overlooked in web development."
    },
    {
        "id": 62,
        "type": "multiple_choice",
        "question": "Which design practice MOST improves scalability?",
        "options": [
            "Fixed layouts",
            "Modular codebase",
            "Inline styles",
            "Embedded scripts"
        ],
        "correct_answer": 1,
        "explanation": "Modular code can be easily extended, reused, and optimized, making it easier to scale applications as requirements grow."
    },
    {
        "id": 63,
        "type": "multiple_choice",
        "question": "Why is testing across devices essential?",
        "options": [
            "Devices are similar",
            "User contexts vary",
            "It reduces CSS",
            "It removes JavaScript"
        ],
        "correct_answer": 1,
        "explanation": "Users access websites on diverse devices with different screen sizes, capabilities, and contexts—testing ensures quality across all."
    },
    {
        "id": 64,
        "type": "multiple_choice",
        "question": "Which principle MOST supports future maintenance?",
        "options": [
            "Fast coding",
            "Clean architecture",
            "Inline scripts",
            "Fixed designs"
        ],
        "correct_answer": 1,
        "explanation": "Clean, well-organized architecture makes code understandable and modifiable, reducing the cost and effort of future maintenance."
    },
    {
        "id": 65,
        "type": "multiple_choice",
        "question": "Which factor MOST improves security posture?",
        "options": [
            "Styling",
            "Server-side validation",
            "Fonts",
            "Layout"
        ],
        "correct_answer": 1,
        "explanation": "Server-side validation is critical for security—it cannot be bypassed by users and provides the final check on all submitted data."
    },
    {
        "id": 66,
        "type": "multiple_choice",
        "question": "Which HTML element groups table rows that contain summary or total values?",
        "options": [
            "<tbody>",
            "<thead>",
            "<tfoot>",
            "<tr>"
        ],
        "correct_answer": 2,
        "explanation": "<tfoot> is specifically designed to contain footer rows in tables, often used for summaries or totals."
    },
    {
        "id": 67,
        "type": "multiple_choice",
        "question": "A table looks cluttered and unreadable. Which solution is BEST?",
        "options": [
            "Adding more columns",
            "Applying CSS spacing and borders",
            "Removing table headers",
            "Using inline HTML formatting"
        ],
        "correct_answer": 1,
        "explanation": "CSS can improve table readability through proper spacing, borders, alternating row colors, and other visual enhancements."
    },
    {
        "id": 68,
        "type": "multiple_choice",
        "question": "Why should CSS be used instead of HTML attributes for table styling?",
        "options": [
            "HTML attributes are faster",
            "CSS improves separation of concerns",
            "CSS prevents table rendering",
            "HTML styling is mandatory"
        ],
        "correct_answer": 1,
        "explanation": "Using CSS for styling maintains separation between content (HTML) and presentation, following modern web development best practices."
    },
    {
        "id": 69,
        "type": "multiple_choice",
        "question": "Which error MOST affects table semantics?",
        "options": [
            "Missing borders",
            "Using <td> instead of <th> for headers",
            "Small font size",
            "Light background color"
        ],
        "correct_answer": 1,
        "explanation": "Using <td> for headers loses semantic meaning—<th> properly identifies header cells for screen readers and browsers."
    },
    {
        "id": 70,
        "type": "multiple_choice",
        "question": "Which statement BEST describes modern table usage?",
        "options": [
            "Tables are obsolete",
            "Tables should be used only for tabular data",
            "Tables are best for layouts",
            "Tables replace CSS Grid"
        ],
        "correct_answer": 1,
        "explanation": "Tables remain essential for tabular data but should not be used for page layout—that's what CSS Grid and Flexbox are for."
    },
    {
        "id": 71,
        "type": "multiple_choice",
        "question": "What is the advantage of using relative links within a website?",
        "options": [
            "They load faster",
            "They are easier to maintain when files move",
            "They prevent hacking",
            "They replace absolute links"
        ],
        "correct_answer": 1,
        "explanation": "Relative links reference files based on current location, making sites portable and easier to maintain when directories change."
    },
    {
        "id": 72,
        "type": "multiple_choice",
        "question": "Which link type connects to another website?",
        "options": [
            "Internal link",
            "Anchor link",
            "External link",
            "Bookmark link"
        ],
        "correct_answer": 2,
        "explanation": "External links point to resources on different domains or websites, using absolute URLs."
    },
    {
        "id": 73,
        "type": "multiple_choice",
        "question": "Why is the title attribute useful in links?",
        "options": [
            "It styles the link",
            "It provides additional context on hover",
            "It changes link color",
            "It improves loading speed"
        ],
        "correct_answer": 1,
        "explanation": "The title attribute provides supplementary information about a link, typically displayed as a tooltip on hover."
    },
    {
        "id": 74,
        "type": "multiple_choice",
        "question": "Which design choice MOST improves accessibility for users relying on screen readers?",
        "options": [
            "Using icons only",
            "Meaningful link text",
            "Removing underlines",
            "Using images without text"
        ],
        "correct_answer": 1,
        "explanation": "Descriptive link text tells screen reader users where links go, unlike vague text like 'click here'."
    },
    {
        "id": 75,
        "type": "multiple_choice",
        "question": "Which statement BEST reflects good link design practice?",
        "options": [
            "Links should open in new tabs always",
            "Links should clearly indicate their destination",
            "All links should be images",
            "Links should replace buttons"
        ],
        "correct_answer": 1,
        "explanation": "Clear, descriptive link text helps users understand where they'll go before clicking, improving usability and accessibility."
    },
    {
        "id": 76,
        "type": "multiple_choice",
        "question": "A user disables JavaScript and successfully submits invalid data to the server. This shows JavaScript validation can be bypassed.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "JavaScript runs client-side and can be disabled or bypassed—never rely on it alone for security or validation."
    },
    {
        "id": 77,
        "type": "multiple_choice",
        "question": "JavaScript validation prevents all security threats in web applications.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 1,
        "explanation": "JavaScript only provides client-side validation and cannot prevent server-side attacks or data manipulation."
    },
    {
        "id": 78,
        "type": "multiple_choice",
        "question": "Poorly written CSS increases debugging and maintenance effort.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 0,
        "explanation": "Disorganized CSS with high specificity, duplication, or !important overrides becomes difficult to debug and maintain."
    },
    {
        "id": 79,
        "type": "multiple_choice",
        "question": "A website uses absolute positioning for all elements and still adapts well to screen size changes. This approach supports responsive design.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 1,
        "explanation": "Absolute positioning removes elements from normal flow and typically doesn't adapt well to different screen sizes."
    },
    {
        "id": 80,
        "type": "multiple_choice",
        "question": "A developer expects JavaScript code to run without any user action or browser event. This expectation is always correct.",
        "options": [
            "True",
            "False"
        ],
        "correct_answer": 1,
        "explanation": "JavaScript runs in response to events or when scripts load—it doesn't execute without some trigger."
    },
    {
        "id": 81,
        "type": "multiple_choice",
        "question": "External CSS files are linked to HTML using the ____ tag.",
        "options": [
            "<style>",
            "<css>",
            "<link>",
            "<script>"
        ],
        "correct_answer": 2,
        "explanation": "The <link> tag, typically in the <head> section, connects external CSS files to HTML documents."
    },
    {
        "id": 82,
        "type": "multiple_choice",
        "question": "PHP is commonly used together with ____ to store and retrieve data.",
        "options": [
            "HTML",
            "MySQL",
            "CSS",
            "JavaScript"
        ],
        "correct_answer": 1,
        "explanation": "PHP frequently pairs with MySQL databases for dynamic data storage and retrieval in web applications."
    },
    {
        "id": 83,
        "type": "multiple_choice",
        "question": "Separating HTML, CSS, JavaScript, and PHP into different files follows the principle of ____.",
        "options": [
            "Modular design",
            "Separation of Concerns",
            "Layered architecture",
            "Component isolation"
        ],
        "correct_answer": 1,
        "explanation": "Separation of Concerns divides a program into distinct sections, each handling a specific aspect (structure, presentation, behavior)."
    },
    {
        "id": 84,
        "type": "multiple_choice",
        "question": "The HTML element used to define the header section of a webpage is called ____.",
        "options": [
            "<head>",
            "<header>",
            "<h1>",
            "<top>"
        ],
        "correct_answer": 1,
        "explanation": "<header> is a semantic HTML5 element for introductory content or navigation links at the top of a page or section."
    },
    {
        "id": 85,
        "type": "multiple_choice",
        "question": "The HTML element used to create an unordered list is ____.",
        "options": [
            "<ol>",
            "<ul>",
            "<li>",
            "<list>"
        ],
        "correct_answer": 1,
        "explanation": "<ul> (unordered list) creates bulleted lists, with each item marked by <li> tags."
    },
    {
        "id": 86,
        "type": "multiple_choice",
        "question": "Why should JavaScript be placed at the bottom of pages or deferred?",
        "options": [
            "To improve accessibility",
            "To prevent blocking rendering",
            "To reduce HTML size",
            "To enhance CSS"
        ],
        "correct_answer": 1,
        "explanation": "JavaScript at the bottom or deferred prevents blocking HTML parsing and rendering, improving perceived page load speed."
    },
    {
        "id": 87,
        "type": "multiple_choice",
        "question": "PHP improves security by:",
        "options": [
            "Styling forms",
            "Sanitizing server-side input",
            "Managing CSS",
            "Controlling layouts"
        ],
        "correct_answer": 1,
        "explanation": "Server-side input sanitization in PHP prevents SQL injection, XSS attacks, and other security vulnerabilities."
    },
    {
        "id": 88,
        "type": "multiple_choice",
        "question": "Which PHP role is essential in form handling?",
        "options": [
            "Styling inputs",
            "Processing submitted data",
            "Validating HTML",
            "Executing JavaScript"
        ],
        "correct_answer": 1,
        "explanation": "PHP receives, validates, and processes form data sent from browsers, making it essential for form handling."
    },
    {
        "id": 89,
        "type": "multiple_choice",
        "question": "Which design choice best supports long-term system upgrades?",
        "options": [
            "Inline code",
            "Modular architecture",
            "Hard-coded logic",
            "Embedded styles"
        ],
        "correct_answer": 1,
        "explanation": "Modular architecture allows components to be updated or replaced independently without breaking the entire system."
    },
    {
        "id": 90,
        "type": "multiple_choice",
        "question": "A system fails under heavy user load. Which layer is MOST responsible?",
        "options": [
            "HTML structure",
            "Backend processing",
            "CSS styling",
            "Browser cache"
        ],
        "correct_answer": 1,
        "explanation": "Backend processing handles concurrent requests—poor architecture here leads to failures under heavy load."
    },
    {
        "id": 91,
        "type": "multiple_choice",
        "question": "Which layer MOST affects first-time user experience?",
        "options": [
            "Database",
            "Frontend design",
            "Server configuration",
            "Hosting provider"
        ],
        "correct_answer": 1,
        "explanation": "First impressions come from visual design, layout, and initial interactions—all part of frontend experience."
    },
    {
        "id": 92,
        "type": "multiple_choice",
        "question": "Which practice MOST reduces technical debt?",
        "options": [
            "Copy-paste coding",
            "Modular and reusable components",
            "Inline scripts",
            "Fixed layouts"
        ],
        "correct_answer": 1,
        "explanation": "Modular, reusable code prevents duplication and makes future changes easier, reducing technical debt accumulation."
    },
    {
        "id": 93,
        "type": "multiple_choice",
        "question": "A system must scale to thousands of users. Which factor is MOST critical?",
        "options": [
            "CSS animations",
            "Backend efficiency",
            "HTML comments",
            "Image sizes only"
        ],
        "correct_answer": 1,
        "explanation": "Efficient backend processing, database queries, and server architecture determine how well a system scales to many users."
    },
    {
        "id": 94,
        "type": "multiple_choice",
        "question": "Which strategy MOST improves usability testing results?",
        "options": [
            "Complex UI",
            "User-centered design",
            "Fixed layouts",
            "Inline scripts"
        ],
        "correct_answer": 1,
        "explanation": "User-centered design focuses on real user needs and behaviors, leading to better usability testing outcomes."
    },
    {
        "id": 95,
        "type": "multiple_choice",
        "question": "Why should backend logic remain hidden from users?",
        "options": [
            "To improve styling",
            "To protect security and integrity",
            "To enhance UI",
            "To reduce load time"
        ],
        "correct_answer": 1,
        "explanation": "Exposed backend logic reveals vulnerabilities, database structures, and implementation details that attackers could exploit."
    },
    {
        "id": 96,
        "type": "multiple_choice",
        "question": "When designing a scalable academic website, which HTML structure best supports future expansion?",
        "options": [
            "Table-based layout",
            "Flat document structure",
            "Semantic and modular structure",
            "Inline elements only"
        ],
        "correct_answer": 2,
        "explanation": "Semantic, modular HTML provides clear structure that can be easily extended and maintained as the site grows."
    },
    {
        "id": 97,
        "type": "multiple_choice",
        "question": "A form-based system frequently submits incomplete data. Which HTML design decision would best support reliable backend processing?",
        "options": [
            "Using GET instead of POST",
            "Adding proper name attributes",
            "Styling inputs with CSS",
            "Embedding JavaScript alerts"
        ],
        "correct_answer": 1,
        "explanation": "Name attributes identify form fields on the server—without them, submitted data cannot be properly processed."
    },
    {
        "id": 98,
        "type": "multiple_choice",
        "question": "A large project's CSS becomes difficult to maintain. Which architectural approach prevents this?",
        "options": [
            "Inline styles",
            "Modular CSS structure",
            "Duplicate selectors",
            "Embedded CSS"
        ],
        "correct_answer": 1,
        "explanation": "Modular CSS (like BEM, SMACSS) organizes styles into manageable, reusable components that are easier to maintain."
    },
    {
        "id": 99,
        "type": "multiple_choice",
        "question": "Why does separating layout and typography styles improve scalability?",
        "options": [
            "It reduces file size",
            "It simplifies redesigns",
            "It improves HTML parsing",
            "It disables JavaScript"
        ],
        "correct_answer": 1,
        "explanation": "Separated concerns allow redesigns to change typography or layout independently without rewriting everything."
    },
    {
        "id": 100,
        "type": "multiple_choice",
        "question": "JavaScript improves user experience primarily by:",
        "options": [
            "Styling pages",
            "Enabling dynamic interaction",
            "Connecting databases",
            "Creating layouts"
        ],
        "correct_answer": 1,
        "explanation": "JavaScript enables real-time updates, interactive features, and dynamic content that responds to user actions."
    },
    {
        "id": 101,
        "type": "multiple_choice",
        "question": "Why should JavaScript validation complement PHP validation?",
        "options": [
            "JavaScript replaces PHP",
            "PHP runs in the browser",
            "JavaScript provides immediate feedback",
            "PHP handles client-side validation"
        ],
        "correct_answer": 2,
        "explanation": "JavaScript gives instant feedback without server round-trips, improving user experience while PHP ensures final security."
    },
    {
        "id": 102,
        "type": "multiple_choice",
        "question": "Which principle guides ethical web development?",
        "options": [
            "Performance only",
            "Accessibility and inclusivity",
            "Styling consistency",
            "Browser exclusivity"
        ],
        "correct_answer": 1,
        "explanation": "Ethical web development ensures websites are accessible to all users regardless of abilities, devices, or circumstances."
    },
    {
        "id": 103,
        "type": "multiple_choice",
        "question": "Why is documentation critical in web projects?",
        "options": [
            "It replaces code",
            "It supports maintenance and onboarding",
            "It improves CSS",
            "It reduces HTML"
        ],
        "correct_answer": 1,
        "explanation": "Documentation helps new developers understand the project and enables efficient maintenance over time."
    },
    {
        "id": 104,
        "type": "multiple_choice",
        "question": "Which factor MOST affects future upgrades?",
        "options": [
            "Inline code",
            "Flexible architecture",
            "Hard-coded logic",
            "Fixed layouts"
        ],
        "correct_answer": 1,
        "explanation": "Flexible architecture accommodates changes and new requirements without requiring complete rewrites."
    },
    {
        "id": 105,
        "type": "multiple_choice",
        "question": "Which development approach MOST aligns with professional practice?",
        "options": [
            "Trial-and-error coding",
            "Structured, standards-based development",
            "Inline scripting",
            "Minimal testing"
        ],
        "correct_answer": 1,
        "explanation": "Professional development follows structured processes, standards, and testing to ensure quality and reliability."
    },
    {
        "id": 106,
        "type": "multiple_choice",
        "question": "Which approach BEST supports collaborative assessment?",
        "options": [
            "Individual coding styles",
            "Standardized structure",
            "Inline scripts",
            "Hard-coded logic"
        ],
        "correct_answer": 1,
        "explanation": "Standardized code structure enables team members to review, understand, and assess each other's work effectively."
    },
    {
        "id": 107,
        "type": "multiple_choice",
        "question": "A project scales poorly. Which factor was MOST neglected?",
        "options": [
            "CSS animations",
            "Backend architecture",
            "HTML comments",
            "Fonts"
        ],
        "correct_answer": 1,
        "explanation": "Scalability issues typically stem from backend architecture decisions—database design, server logic, and infrastructure."
    },
    {
        "id": 108,
        "type": "multiple_choice",
        "question": "Which design approach BEST supports real-world deployment?",
        "options": [
            "Experimental coding",
            "Standards-compliant architecture",
            "Inline styling",
            "Hard-coded logic"
        ],
        "correct_answer": 1,
        "explanation": "Standards compliance ensures compatibility with diverse real-world environments, browsers, and devices."
    },
    {
        "id": 109,
        "type": "multiple_choice",
        "question": "Why should presentation logic be separated from data logic?",
        "options": [
            "To increase file size",
            "To improve maintainability",
            "To reduce accessibility",
            "To slow execution"
        ],
        "correct_answer": 1,
        "explanation": "Separation allows each layer to be modified independently without affecting the other, improving maintainability."
    },
    {
        "id": 110,
        "type": "multiple_choice",
        "question": "Which development mindset MOST aligns with professional web engineering?",
        "options": [
            "Quick fixes",
            "Long-term maintainability",
            "Inline scripting",
            "Minimal documentation"
        ],
        "correct_answer": 1,
        "explanation": "Professional engineering prioritizes sustainable, maintainable solutions over quick fixes that create technical debt."
    },
    
    
    
    {
        "id": 111,
        "type": "multiple_choice",
        "question": "A university website is failing accessibility audits and ranking poorly on search engines. Which HTML redesign decision would MOST effectively address both issues?",
        "options": [
            "Replacing <div> tags with semantic elements",
            "Increasing font sizes using inline styles",
            "Embedding JavaScript inside HTML",
            "Using tables for page layout"
        ],
        "correct_answer": 0,
        "explanation": "Semantic HTML (like <header>, <nav>, <main>, <article>) improves accessibility for screen readers and helps search engines better understand content structure, improving both accessibility and SEO simultaneously."
    },
    {
        "id": 112,
        "type": "multiple_choice",
        "question": "A large web project involves multiple developers. Which HTML practice best supports collaboration and long-term maintenance?",
        "options": [
            "Using deeply nested <div> elements",
            "Writing inline HTML styles",
            "Applying semantic HTML structure",
            "Embedding PHP directly in HTML"
        ],
        "correct_answer": 2,
        "explanation": "Semantic HTML creates self-documenting code that all developers can understand intuitively, reducing confusion and making maintenance easier across team members."
    },
    {
        "id": 113,
        "type": "multiple_choice",
        "question": "A multilingual website struggles with search indexing. Which HTML attribute strategy best resolves this?",
        "options": [
            "lang attribute usage",
            "id attribute consistency",
            "class naming",
            "Inline metadata"
        ],
        "correct_answer": 0,
        "explanation": "The lang attribute tells search engines and browsers which language content is written in, improving international SEO and enabling proper pronunciation by screen readers."
    },
    {
        "id": 114,
        "type": "multiple_choice",
        "question": "A website breaks on tablets but works on desktops. Which CSS strategy best fixes this issue?",
        "options": [
            "Fixed widths",
            "Media queries",
            "Inline styling",
            "Absolute positioning"
        ],
        "correct_answer": 1,
        "explanation": "Media queries allow CSS to apply different styles based on device characteristics like screen width, enabling proper display across tablets, phones, and desktops."
    },
    {
        "id": 115,
        "type": "multiple_choice",
        "question": "Why is Flexbox preferred over floats for modern layouts?",
        "options": [
            "Floats load faster",
            "Flexbox handles alignment dynamically",
            "Floats support responsiveness better",
            "Flexbox removes the need for HTML"
        ],
        "correct_answer": 1,
        "explanation": "Flexbox provides powerful, dynamic alignment and distribution capabilities that adapt to content size and screen dimensions, unlike floats which were designed for text wrapping."
    },
    {
        "id": 116,
        "type": "multiple_choice",
        "question": "Absolute positioning negatively impacts responsiveness because it:",
        "options": [
            "Ignores screen size changes",
            "Breaks JavaScript",
            "Disables HTML semantics",
            "Removes accessibility"
        ],
        "correct_answer": 0,
        "explanation": "Absolutely positioned elements are removed from normal document flow and positioned relative to their nearest positioned ancestor, making them unresponsive to screen size changes."
    },
    {
        "id": 117,
        "type": "multiple_choice",
        "question": "A form submits invalid data repeatedly. Which JavaScript strategy best prevents this?",
        "options": [
            "Server-side validation only",
            "Client-side validation before submission",
            "Removing form constraints",
            "Using CSS validation"
        ],
        "correct_answer": 1,
        "explanation": "Client-side validation provides immediate feedback to users before submission, preventing unnecessary server requests and improving user experience by catching errors instantly."
    },
    {
        "id": 118,
        "type": "multiple_choice",
        "question": "Why is event-driven programming essential in modern web apps?",
        "options": [
            "It reduces HTML size",
            "It responds dynamically to user actions",
            "It replaces CSS",
            "It improves database speed"
        ],
        "correct_answer": 1,
        "explanation": "Event-driven programming allows web applications to react to user interactions (clicks, keystrokes, form submissions) in real-time, creating dynamic and interactive experiences."
    },
    {
        "id": 119,
        "type": "multiple_choice",
        "question": "Why is PHP classified as server-side scripting?",
        "options": [
            "It runs in the browser",
            "It executes before content reaches the client",
            "It styles pages",
            "It handles CSS"
        ],
        "correct_answer": 1,
        "explanation": "PHP executes on the web server before any content is sent to the browser, generating HTML dynamically and handling server-side operations like database access."
    },
    {
        "id": 120,
        "type": "multiple_choice",
        "question": "A login system works locally but fails online. Which PHP issue is MOST likely?",
        "options": [
            "HTML validation",
            "Server configuration",
            "CSS conflicts",
            "JavaScript errors"
        ],
        "correct_answer": 1,
        "explanation": "Differences in PHP versions, enabled extensions, error reporting settings, or database configurations between local and production servers commonly cause login failures."
    },
    {
        "id": 121,
        "type": "multiple_choice",
        "question": "Why should PHP files not expose logic to users?",
        "options": [
            "PHP runs client-side",
            "PHP executes before response",
            "PHP improves accessibility",
            "PHP handles CSS"
        ],
        "correct_answer": 1,
        "explanation": "PHP executes entirely on the server, so only its output (HTML) reaches the browser—the actual PHP code remains hidden from users, protecting application logic and security."
    },
    {
        "id": 122,
        "type": "multiple_choice",
        "question": "A dynamic website fails when JavaScript is disabled. Which design principle was ignored?",
        "options": [
            "Graceful degradation",
            "Inline styling",
            "Server caching",
            "Fixed layout"
        ],
        "correct_answer": 0,
        "explanation": "Graceful degradation ensures core functionality works even when advanced features fail—without it, sites become completely unusable when JavaScript is disabled."
    },
    {
        "id": 123,
        "type": "multiple_choice",
        "question": "Why is separation of concerns important in web development?",
        "options": [
            "It reduces browser compatibility",
            "It improves maintainability and scalability",
            "It increases page size",
            "It limits functionality"
        ],
        "correct_answer": 1,
        "explanation": "Separating HTML (structure), CSS (presentation), and JavaScript (behavior) makes code easier to understand, debug, and modify independently, improving long-term maintainability."
    },
    {
        "id": 124,
        "type": "multiple_choice",
        "question": "A university portal redesign focuses on accessibility, performance, and scalability. Which combined approach best meets these goals?",
        "options": [
            "Table layouts and inline CSS",
            "Semantic HTML, external CSS, modular JS, server-side PHP",
            "JavaScript-only rendering",
            "Embedded styles and scripts"
        ],
        "correct_answer": 1,
        "explanation": "Semantic HTML aids accessibility, external CSS improves performance, modular JavaScript enables scalability, and server-side PHP ensures reliable processing—a comprehensive approach."
    },
    {
        "id": 125,
        "type": "multiple_choice",
        "question": "A site works visually but fails usability testing. Which area was MOST neglected?",
        "options": [
            "Backend logic",
            "User experience and accessibility",
            "Database structure",
            "Server hosting"
        ],
        "correct_answer": 1,
        "explanation": "Visual design alone doesn't guarantee usability—factors like intuitive navigation, clear feedback, and accessibility for all users determine real-world usability."
    },
    {
        "id": 126,
        "type": "multiple_choice",
        "question": "Why is accessibility a core quality metric in web development?",
        "options": [
            "It improves aesthetics",
            "It ensures inclusivity and legal compliance",
            "It reduces server load",
            "It replaces usability"
        ],
        "correct_answer": 1,
        "explanation": "Accessibility ensures people with disabilities can use websites, which is both ethically important and legally required in many jurisdictions (like Section 508, ADA, WCAG)."
    },
    {
        "id": 127,
        "type": "multiple_choice",
        "question": "Which development choice MOST improves maintainability?",
        "options": [
            "Inline styling",
            "Clear separation of technologies",
            "Embedded scripts",
            "Table layouts"
        ],
        "correct_answer": 1,
        "explanation": "Clear separation of HTML, CSS, and JavaScript allows each layer to be modified independently without unintended side effects, making maintenance significantly easier."
    },
    {
        "id": 128,
        "type": "multiple_choice",
        "question": "Which practice BEST ensures long-term project success?",
        "options": [
            "Rapid coding",
            "Standards-based development",
            "Hard-coded solutions",
            "Minimal documentation"
        ],
        "correct_answer": 1,
        "explanation": "Following web standards ensures compatibility with future browsers and devices, making projects more sustainable and adaptable over the long term."
    },
    {
        "id": 129,
        "type": "multiple_choice",
        "question": "A poorly structured project MOST affects which phase?",
        "options": [
            "Deployment",
            "Maintenance",
            "Hosting",
            "Rendering"
        ],
        "correct_answer": 1,
        "explanation": "Poor structure makes maintenance extremely difficult and costly—fixing bugs, adding features, and understanding code become time-consuming and error-prone."
    },
    {
        "id": 130,
        "type": "multiple_choice",
        "question": "Which technology combination BEST supports interactive, secure websites?",
        "options": [
            "HTML + CSS",
            "HTML + CSS + JavaScript + PHP",
            "CSS + PHP",
            "JavaScript only"
        ],
        "correct_answer": 1,
        "explanation": "This full stack provides structure (HTML), presentation (CSS), client-side interaction (JavaScript), and server-side security/processing (PHP)—all essential for modern web apps."
    },
    {
        "id": 131,
        "type": "multiple_choice",
        "question": "A website fails compliance audits. Which aspect was MOST likely ignored?",
        "options": [
            "Color schemes",
            "Accessibility standards",
            "Image resolution",
            "Fonts"
        ],
        "correct_answer": 1,
        "explanation": "Accessibility standards (like WCAG 2.1) are common compliance requirements that are frequently overlooked, leading to failed audits and potential legal issues."
    },
    {
        "id": 132,
        "type": "multiple_choice",
        "question": "Which design practice MOST improves scalability?",
        "options": [
            "Fixed layouts",
            "Modular codebase",
            "Inline styles",
            "Embedded scripts"
        ],
        "correct_answer": 1,
        "explanation": "A modular codebase allows components to be developed, tested, and scaled independently, making it easier to handle growth in features and user traffic."
    },
    {
        "id": 133,
        "type": "multiple_choice",
        "question": "Why is testing across devices essential?",
        "options": [
            "Devices are similar",
            "User contexts vary",
            "It reduces CSS",
            "It removes JavaScript"
        ],
        "correct_answer": 1,
        "explanation": "Users access websites on diverse devices with different screen sizes, capabilities, and contexts—testing ensures quality experiences across this variety."
    },
    {
        "id": 134,
        "type": "multiple_choice",
        "question": "Which principle MOST supports future maintenance?",
        "options": [
            "Fast coding",
            "Clean architecture",
            "Inline scripts",
            "Fixed designs"
        ],
        "correct_answer": 1,
        "explanation": "Clean architecture with well-organized, loosely coupled components makes future maintenance significantly easier by reducing complexity and dependencies."
    },
    {
        "id": 135,
        "type": "multiple_choice",
        "question": "Which factor MOST improves security posture?",
        "options": [
            "Styling",
            "Server-side validation",
            "Fonts",
            "Layout"
        ],
        "correct_answer": 1,
        "explanation": "Server-side validation is the most critical security measure—unlike client-side validation, it cannot be bypassed and provides the final defense against malicious input."
    }

    

]
}