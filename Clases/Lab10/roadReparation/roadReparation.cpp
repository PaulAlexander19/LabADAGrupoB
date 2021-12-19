
  
/*
 * @Autor: Luque Ccosi, Paul Alexander
 * @Ejercicio: Road reparation
 * Lab 10
 * @Descripcion: calcular el costo que nesesario , para reparar del so caminos de cirto numero de cuidades relacionadas
*/

#include<iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

//  Arista
struct Arista{
  int inicio;
  int llegada;
  ll peso;
};

const int maxM = 2e5;
vector<Arista> data;

// saber que aristas ya estan relacionadas
int parnert[maxM];
int n, m;

// ordenar el vector
bool comp(Arista a, Arista b){
  return a.peso < b.peso;
}

// encontraremos, al valor al que ya esta relacionado
int find (int i){
  if(parnert[i] == -1){
    return i;
  }

  parnert[i] = find(parnert[i]);
  return parnert[i];
}


// merge relaciona a las cuidades
bool merge(int a, int b){
  a = find(a);
  b = find(b);

  //  relacionados con anterioridad
  if(a == b){
    return false; 
  } 

  parnert[a] = b;
  return true;
}


int main() {
  ll count = 0; // cuenta la cantidad de peso usados
  int numsAristas = 0; // cuenta la cantidad de aristas usadas
  // ingreso de datos
  cin >> n;
  cin >> m;

  // llenado de datos de parnert
  for(int i = 0; i < n; i++) parnert[i] = -1;

  for(int i = 0; i < m; i++){
    int a , b;
    ll c;
    cin >> a;
    cin >> b;
    cin >> c;
    data.push_back({a,b,c});
  }
  // ordenamientod del vector, para poder trabajarlo de mejor manera , haremos uso de comp ya que es la funcion mediante la que se ordena
  sort(data.begin(), data.end(), comp);
  
  for(Arista a : data){
    if(merge(a.inicio, a.llegada)){ // evaluamos que no esten conectadas 
      count += a.peso; 
      numsAristas++; 
    }
  }


  if(numsAristas == (n - 1)){
    cout << count;
  }
  else {
    cout << "IMPOSSIBLE";
  }

  return 0;
}
