/*
 * @Autor: Luque Ccosi, Paul Alexander
 * @Ejercicio: LongestFlightRoute
 * Lab 10
 * @Descripcion: Uolevi ha ganado un concurso, y el premio es un vuelo gratuito que puede consistir en uno o más vuelos por ciudades. Por supuesto, Uolevi quiere elegir un viaje que tenga tantas ciudades como sea posible. Uolevi quiere volar de Syrjälä a Lehmälä para visitar el número máximo de ciudades. Se le da la lista de vuelos posibles y sabe que no hay ciclos dirigidos en la red de vuelos.
 */

#include <bits/stdc++.h>
using namespace std;
const int MAX = 1e5 + 1;

int n, m;                                 // CANTIDAD DE CIUDADES, CANTIDAD DE RUTAS ENTRE CIUDADES
bool visitedVertexs[MAX];                 // ARREGLO INDENTIFICADOR PARA SABER SI EL VERTICE FUE VISITADO
int in[MAX], p[MAX], l[MAX], answer[MAX]; // ARREGLOS AUXILIARES
vector<int> graph[MAX];                   // ARREGLO DEL GRAFO
queue<int> QUEUE;                         // DECLARAMOS UNA COLA QUE NOS SERVIRA DE APOYO

void algorithmDFS(int ChildNode, int NodeTop)
{ // HALLAREMOS LA RUTA MAS LARGA

  visitedVertexs[ChildNode] = true; // NODO HIJO NO VISITADO DECLARADO CON TRUE
  for (int vertex : graph[ChildNode])
  { // ITERAMOS EN EL GRAFO
    if (vertex != NodeTop && !visitedVertexs[vertex])
    {
      algorithmDFS(vertex, ChildNode);
    }
  }
}

// MAIN
int main()
{

  cin >> n >> m; // INGRESO DE VALORES
  int a, b;      

  for (int i = 0; i < m; i++)
  { // ITERAMOS
    cin >> a >> b;
    graph[a].push_back(b); // INGRESO DE ARISTA DESDE EL ORIGEN HASTA EL DESTINO
    in[b]++;
  }

  algorithmDFS(1, 0);

  if (!visitedVertexs[n])
  {
    cout << "IMPOSSIBLE" << endl;
    return 0;
  }

  fill(l + 2, l + long(MAX), -1); 
  for (int i = 1; i <= n; i++)
  { // ITERAMOS EL GRAFO
    if (in[i] == 0)
    {
      QUEUE.push(i);
    }
  }

  while (!QUEUE.empty())
  { // RECORREMOS LA COLA MIENTRAS NO ESTE VACIA
    int u = QUEUE.front();
    QUEUE.pop();
    for (int v : graph[u])
    { // ITERAMOS LISTA DE ADYACENCIA Y NODOS HIJOS
      if (l[u] != -1 && l[v] < l[u] + 1)
      {
        l[v] = l[u] + 1;
        p[v] = u;
      }
      in[v]--;
      if (in[v] == 0)
      { 
        QUEUE.push(v);
      }
    }
  }
  int resultingRoutes = l[n] - l[1];   // CAMINOS MENOS RUTAS PARA LLEGAR A N
  cout << resultingRoutes + 1 << endl; 

  for (int i = resultingRoutes, u = n; i >= 0; i--)
  {
    answer[i] = u;
    u = p[u];
  }

  for (int i = 0; i <= resultingRoutes; i++)
  {
    cout << answer[i] << " ";
  }
}
