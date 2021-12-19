
  
/*
 * @Autor: Luque Ccosi, Paul Alexander
 * @Ejercicio: shortest Routes I
 * Lab 10
 * @Descripcion: calcular la ruta más corta las distiintas cuidades
*/

#include<iostream>
#include <bits/stdc++.h>

using namespace std;
typedef long long ll;
const int maxNode = 1e5;

// estructuras 
struct Arista{
  int conection;
  ll peso;
};

struct Nodo{
  int indice;
  ll distance;
  friend bool operator<(const Nodo &a, const Nodo &b){
    return a.distance > b.distance;
  };
};

// creacion de variables
int n, m;
ll distancias[maxNode];
vector<Arista> conectando [maxNode];
priority_queue<Nodo> data;

int main() {
  // ingreso de datos inciales
  cin >> n;
  cin >> m;
  for(int i = 0; i < m; i++){
    int a, b;
    ll c;
    cin >> a;
    cin >> b;
    cin >> c;
    --a;
    --b;
    conectando[a].push_back({b, c}); //agregnado los valores al vector, si tiene más de una salida se ordenaran en el orden que se ingresar
  }

  // vertice es como una tabla hash
  memset(distancias, 0x3f, sizeof(distancias)); // llenando el vertice de distancias
  distancias[0] = 0;
  data.push({0,0});

  while(!data.empty()){ // mientras que el nuestra cola de priority_queue no este vacia
    ll d = data.top().distance; 
    int u = data.top().indice; 
    data.pop(); 

    if(d > distancias[u]){ // si el valor de 'd' es mayor al que esta en el vector de distancias[u] lo salteremos
      continue;
    }

    for(Arista a : conectando[u]){ // recorremos cada artista que este en el vector
      ll x = d + a.peso; 
      if(distancias[a.conection] > x){ 
        distancias[a.conection] = x; 
        data.push({a.conection, x});// agremaos el a la  priority_queue
      }
    }
  }

  // impresion de los valores
  for(int i = 0; i < n; i++){
    cout << distancias[i] <<" ";
  }

  return 0;
}
