// Review of Time Complexity
// Q1: What is the time complexity of
for (i = 0; i < n; i++) {
    statement;
}

// La complejidad temporal de este algoritmo es O(n) porque el bucle se ejecuta n veces.

    // A1: O(n)
    for (i = 0; i < n; i++) {   // n + 1 
        statement;               // n
    }

//-------------------------------------------

// Q2: What is the time complexity of
for (i = n; i > 0; i--) {
    statement;
}

// la complejidad temporal de este algoritmo es O(n) porque el bucle se ejecuta n veces.

    // A2: O(n)


// -------------------------------------------

// Q3: What is the time complexity of
for (i = 0; i < n; i=i+5) {
    statement;
}

// la complejidad temporal de este algotimo es O(n/5) pero se pude trabajar con O(n).

// -------------------------------------------

// Q4: What is the time complexity of
for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++) {
        statement;
    }
}

// La complejidad temporal de este algoritmo es O(n^2) porque el bucle se ejecuta n veces y dentro de cada bucle se ejecuta n veces.

    // A4: O(n^2)
    for (i = 0; i < n; i++) {       // n + 1
        for (j = 0; j < n; j++) {   // n * (n + 1)
            statement;              // n * n
            cout << "i" << '\n';
    }
}

// -------------------------------------------

// Q5: What is the time complexity of
for (i = 0; i < n; i++) {
    for (j = 0; j < i; j++) {
        statement;
    }
}

// la complejidad del algoritmo es o(n^2) ya que el buble superior se ejecuta n veces
// pero el buble interior se ejecuta la cantidad de i veces en un punto llegara que i sera cerca a n y por lo tanto
// j recorrera n veces 

    // A5: 
    // Tracing the values of the variables
    //  i   j      no of times
    // ------------------------
    //  0   0 ❌     0
    // ------------------------
    //  1   0 ✔️     1
    //      1 ❌     
    // ------------------------
    //  2   0 ✔️     2
    //      1 ✔️  
    //      2 ❌ 
    // ------------------------
    //  .    
    //  .    
    //  .    
    // ------------------------
    //  n             n

    // 1 + 2 + 3 + ... + n = n * (n + 1) / 2    
    // O(n^2)

// -------------------------------------------

// Q6: What is the time complexity of
p = 0
for (i = 1; p <= n; i++) {
    p = p + i;
}

// la complejidad es de O(n^(1/2)) ya que en cada iteración en P se almacena la suma de los primeros "i" numeros
// y esto se rompe cuando la suma pasa n

    // A6:
    //  i       p
    // ------------------------
    //  1       0 + 1 = 1
    //  2       1 + 2
    //  3       1 + 2 + 3
    //  4       1 + 2 + 3 + 4
    //  .    
    //  .    
    //  .    
    //  k       1 + 2 + 3 + 4 + ... + k

    // Assume k > n
    // p = k * (k + 1) / 2
    //               p > n
    // k * (k + 1) / 2 > n
    // k^2 > n
    // k > sqrt(n)
    // O(n^(1/2))

// -------------------------------------------

