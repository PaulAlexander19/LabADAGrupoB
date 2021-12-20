/*
 * @Autor: Luque Ccosi, Paul Alexander
 * @Ejercicio: FlightDiscount
 * Lab 10
 * @Descripcion: Su tarea es encontrar una ruta de vuelo de precio mínimo desde Syrjälä a Metsälä. Tiene un cupón de descuento, con el que puede reducir a la mitad el precio de cualquier vuelo durante la ruta. Sin embargo, solo puede usar el cupón una vez
*/
#include <bits/stdc++.h>
#define int long long
#define MOD 1000000007
#define MAX 1e15
#define MIN -1e13

using namespace std;

int n, m;                                              // NUMERO DE CIUDADES, CANTIDAD DE VUELOS
vector<array<int, 2>> graph[100005], graphAux[100005]; // ARREGLO BIDIMENSIONAL PARA EL GRAFO
int arrCost[100005], costs_rev[100005];                //  ARREGLO PARA LOS COSTOS

void algorithmDijstra(vector<array<int, 2>> graph[], int arrCost[], int root)
{
    set<int> visited;
    priority_queue<array<int, 3>, vector<array<int, 3>>, greater<array<int, 3>>> QUEUE; // COLA DE PRIORIDAD PARA EL LOS COSTOS
    for (int i = 0; i < graph[root].size(); i++)
    {                                                             // ESTABLECEMOS LOS COSTOS INICIALES DE LAS CIUDADES
        QUEUE.push({graph[root][i][1], root, graph[root][i][0]}); 
    }
    for (int i = 0; i < n; i++)
    {
        arrCost[i] = MAX; // INICIALIZAMOS LOS COSTOS CON MAXIMO(INFINITO))
    }
    arrCost[root] = 0;
    visited.insert(root);
    while (!QUEUE.empty())
    {                           
        auto top = QUEUE.top(); 
        QUEUE.pop();
        if (visited.find(top[2]) == visited.end())
        {                                                   // SI LA CIUDAD NO HA SIDO VISITADA
            arrCost[top[2]] = min(arrCost[top[2]], top[0]); // ESTABLECEMOS EL COSTO DE LA CIUDAD CON EL COSTO DEL VUELO
        }
        else
            continue; // SI LA CIUDAD YA HA SIDO VISITADA, CONTINUAMOS CON LA SIGUIENTE CIUDAD

        visited.insert(top[2]);
        for (int i = 0; i < graph[top[2]].size(); i++)
        {
            QUEUE.push({arrCost[top[2]] + graph[top[2]][i][1], top[2], graph[top[2]][i][0]});
        }
    }
}

void dijkstra()
{
    cin >> n >> m; // LEEMOS EL NUMERO DE CIUDADES Y VUELOS
    int a, b, x;
    vector<array<int, 3>> edge;
    for (int i = 0; i < m; i++)
    { 
        cin >> a >> b >> x;
        a--;
        b--;

        edge.push_back({a, b, x}); // GUARDAMOS LOS VUELOS EN EL ARREGLO
        graph[a].push_back({b, x});
        graphAux[b].push_back({a, x});
    }

    algorithmDijstra(graph, arrCost, 0);
    algorithmDijstra(graphAux, costs_rev, n - 1);

    int cost = MAX;

    for (int i = 0; i < m; i++)
    { // RECORREMOS LOS VUELOS
        cost = min(cost, arrCost[edge[i][0]] + costs_rev[edge[i][1]] + edge[i][2] / 2);
    }
    cout << cost << endl; // IMPRIMIMOS EL COSTO
}

int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    dijkstra(); // LLAMAMOS A LA FUNCION PRINCIPAL
    return 0;
}
