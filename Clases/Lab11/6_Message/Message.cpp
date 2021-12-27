// @Autor: Luque Ccosi, Paul Alexander
// @Ejercicio: Message
// Lab 11


#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>
#include <queue>
#include <map>
using namespace std;

vector<string> dic;
map<int, int> cache;

#define iter(it, c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it) // iteraramos sobre un map o un vector
typedef vector<vector<int>> vvi;                                                        // matrices de enteros
map<string, int> all;                                                                   // guardar todas las palabras del diccionario
vvi res;                                                                                // guardar los resultados NODOS
string s;                                                                               // guardar la cadena a analizares

// Aho-Corasick from SuprDewd
struct aho_corasick
{
  struct out_node
  {
    string keyword;                                          // palabra que se encuentra en el nodo
    out_node *next;                                          // siguiente nodo
    out_node(string k, out_node *n) : keyword(k), next(n) {} // constructor
  };
  struct go_node
  {
    map<char, go_node *> next; // siguiente nodo por cada caracter
    out_node *out;             // siguiente nodo por palabra que se encuentra en el nodo
    go_node *fail;             // siguiente nodo por fallo
    go_node()
    {
      out = NULL;  // por defecto
      fail = NULL; 
    }
  };
  go_node *go;
  int N;
  aho_corasick(vector<string> keywords)
  {
    N = keywords.size(); // numero de palabras
    go = new go_node();  // inicializar el arbol
    iter(k, keywords)
    {
      go_node *cur = go;
      iter(c, *k)
          cur = cur->next.find(*c) != cur->next.end() ? cur->next[*c] : (cur->next[*c] = new go_node());
      cur->out = new out_node(*k, cur->out);
    }
    queue<go_node *> q;
    iter(a, go->next) q.push(a->second); 
    while (!q.empty())
    {
      go_node *r = q.front(); // nodo actual
      q.pop();                // sacar nodo de la cola
      iter(a, r->next)
      {                                                         // para cada caracter
        go_node *s = a->second;                                 
        q.push(s);                                              // agregar nodo a la cola
        go_node *st = r->fail;                                  // nodo fallo
        while (st && st->next.find(a->first) == st->next.end()) 
          st = st->fail;                                        // siguiente fallo
        if (!st)
          st = go;                    // fallo por defecto
        s->fail = st->next[a->first]; 
        if (s->fail)
        {
          if (!s->out)
            s->out = s->fail->out;
          else
          {
            out_node *out = s->out;
            while (out->next)
              out = out->next;
            out->next = s->fail->out;
          }
        }
      }
    }
  }
  vvi search(string s)
  {
    vvi ress(N); // resultados por palabra
    go_node *cur = go;
    iter(c, s)
    {
      while (cur && cur->next.find(*c) == cur->next.end())
        cur = cur->fail;
      if (!cur)
        cur = go;
      cur = cur->next[*c];
      if (!cur)
        cur = go;
      for (out_node *out = cur->out; out; out = out->next)
      {
        ress[all[out->keyword]].push_back(c - s.begin() - out->keyword.size() + 1);
      }
    }
    return ress;
  }
};

int solve(int p)
{
  if (s.size() == p)  // si ya se encontró la palabra
    return 0;           // no hay subcadenas superpuestas
  if (cache.count(p)) // si ya se calculó el resultado
    return cache[p];    // devolver el resultado
  int ans = 0;
  for (int i = 0; i < dic.size(); i++)
  {
    vector<int> &ac = res[all[dic[i]]];
    int it = -1;
    for (int j = 0; j < ac.size(); j++)
    {
      if (ac[j] >= p)
      {
        it = ac[j]; // encontrar la primera posicion de la palabra
        break;
      }
    }
    if (it != -1)
      ans = max(ans, 1 + solve(it + dic[i].size())); // si se encontró la palabra
  }
  return cache[p] = ans;
}

int main()
{
  string t;  // para guardar la cadena a analizar
  int i = 0; // para guardar el numero de la palabra
  while (cin >> s && s[0] != '#')
  {
    dic.push_back(s);
    all[s] = i++;
  }
  while (cin >> s && s[0] != '#')
  {
    while (s[s.size() - 1] != '|')
    {
      cin >> t;
      s.append(t);
    }
    s = s.substr(0, s.size() - 1); // quitar el | final de la cadena
    
    aho_corasick AC(dic);     
    cache.clear();            
    res = AC.search(s);       
    cout << solve(0) << endl;
  }

  return 0;
}