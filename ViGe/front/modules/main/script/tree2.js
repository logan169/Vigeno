/*
var treeData = [
  {
    "name": "Annotation",
    "parent": "null",
    "children": [
      {
        "name": "Gene",
        "parent": "Annotation",
        "children": [
          {
            "name": "Exon",
            "parent": "Gene",
            "children": [
            {
              "name": " 1",
              "parent": "Exon"
            },
            {
              "name": " 2",
              "parent": "Exon"
            },
            {
              "name": " 3",
              "parent": "Exon"
            },
            ]
          },
          {
            "name": "Intron",
            "parent": "Gene",
            "children":[
            {
              "name": " 4",
              "parent": "Exon"
            }
            ]
          },
          {
            "name": "UTR",
            "parent": "Gene",
            "children":[
            {
              "name": " 7",
              "parent": "Exon"
            }
            ]
          }
        ]
      },

      {
        "name": "Intergene",
        "parent": "Annotation",
        "children":[
                     {
            "name": "6",
            "parent": "Intergene"
          }
          ]
      }
    ]
  }
];
*/

//var treeData=[{'color': 'lightsteelblue', 'children_length': 22, 'name': 'chromosome', 'parent': 'null', '_children': [{'color': 'lightsteelblue', 'children_length': 4, 'name': '20', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 9, 'parent': '20'}, {'color': '#FFF', 'name': 27, 'parent': '20'}, {'color': 'lightsteelblue', 'name': 81, 'parent': '20'}, {'color': 'lightsteelblue', 'name': 92, 'parent': '20'}]}, {'color': '#FFF', 'children_length': 1, 'name': '21', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 13, 'parent': '21'}]}, {'color': 'lightsteelblue', 'children_length': 5, 'name': '22', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 7, 'parent': '22'}, {'color': 'lightsteelblue', 'name': 20, 'parent': '22'}, {'color': 'lightsteelblue', 'name': 32, 'parent': '22'}, {'color': '#FFF', 'name': 52, 'parent': '22'}, {'color': 'lightsteelblue', 'name': 66, 'parent': '22'}]}, {'color': 'lightsteelblue', 'children_length': 7, 'name': '1', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 26, 'parent': '1'}, {'color': '#FFF', 'name': 30, 'parent': '1'}, {'color': 'lightsteelblue', 'name': 36, 'parent': '1'}, {'color': '#FFF', 'name': 46, 'parent': '1'}, {'color': '#FFF', 'name': 80, 'parent': '1'}, {'color': '#FFF', 'name': 83, 'parent': '1'}, {'color': '#FFF', 'name': 89, 'parent': '1'}]}, {'color': 'lightsteelblue', 'children_length': 5, 'name': '3', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 11, 'parent': '3'}, {'color': 'lightsteelblue', 'name': 16, 'parent': '3'}, {'color': '#FFF', 'name': 44, 'parent': '3'}, {'color': '#FFF', 'name': 67, 'parent': '3'}, {'color': 'lightsteelblue', 'name': 90, 'parent': '3'}]}, {'color': 'lightsteelblue', 'children_length': 8, 'name': '2', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 4, 'parent': '2'}, {'color': 'lightsteelblue', 'name': 5, 'parent': '2'}, {'color': '#FFF', 'name': 6, 'parent': '2'}, {'color': 'lightsteelblue', 'name': 43, 'parent': '2'}, {'color': '#FFF', 'name': 51, 'parent': '2'}, {'color': '#FFF', 'name': 57, 'parent': '2'}, {'color': 'lightsteelblue', 'name': 87, 'parent': '2'}, {'color': 'lightsteelblue', 'name': 96, 'parent': '2'}]}, {'color': 'lightsteelblue', 'children_length': 6, 'name': '5', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 45, 'parent': '5'}, {'color': '#FFF', 'name': 48, 'parent': '5'}, {'color': '#FFF', 'name': 65, 'parent': '5'}, {'color': 'lightsteelblue', 'name': 74, 'parent': '5'}, {'color': 'lightsteelblue', 'name': 86, 'parent': '5'}, {'color': 'lightsteelblue', 'name': 95, 'parent': '5'}]}, {'color': '#FFF', 'children_length': 1, 'name': '4', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 3, 'parent': '4'}]}, {'color': 'lightsteelblue', 'children_length': 3, 'name': '7', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 29, 'parent': '7'}, {'color': '#FFF', 'name': 75, 'parent': '7'}, {'color': '#FFF', 'name': 93, 'parent': '7'}]}, {'color': 'lightsteelblue', 'children_length': 7, 'name': '6', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 1, 'parent': '6'}, {'color': '#FFF', 'name': 8, 'parent': '6'}, {'color': '#FFF', 'name': 12, 'parent': '6'}, {'color': '#FFF', 'name': 33, 'parent': '6'}, {'color': '#FFF', 'name': 38, 'parent': '6'}, {'color': '#FFF', 'name': 59, 'parent': '6'}, {'color': 'lightsteelblue', 'name': 88, 'parent': '6'}]}, {'color': 'lightsteelblue', 'children_length': 3, 'name': '9', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 31, 'parent': '9'}, {'color': 'lightsteelblue', 'name': 69, 'parent': '9'}, {'color': '#FFF', 'name': 72, 'parent': '9'}]}, {'color': 'lightsteelblue', 'children_length': 9, 'name': '8', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 2, 'parent': '8'}, {'color': 'lightsteelblue', 'name': 10, 'parent': '8'}, {'color': 'lightsteelblue', 'name': 15, 'parent': '8'}, {'color': 'lightsteelblue', 'name': 56, 'parent': '8'}, {'color': 'lightsteelblue', 'name': 58, 'parent': '8'}, {'color': '#FFF', 'name': 73, 'parent': '8'}, {'color': 'lightsteelblue', 'name': 78, 'parent': '8'}, {'color': '#FFF', 'name': 79, 'parent': '8'}, {'color': '#FFF', 'name': 82, 'parent': '8'}]}, {'color': 'lightsteelblue', 'children_length': 5, 'name': 'X', 'parent': 'chromosome', '__children': [{'color': 'lightsteelblue', 'name': 19, 'parent': 'X'}, {'color': '#FFF', 'name': 35, 'parent': 'X'}, {'color': 'lightsteelblue', 'name': 55, 'parent': 'X'}, {'color': '#FFF', 'name': 60, 'parent': 'X'}, {'color': '#FFF', 'name': 91, 'parent': 'X'}]}, {'color': 'lightsteelblue', 'children_length': 3, 'name': '11', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 61, 'parent': '11'}, {'color': 'lightsteelblue', 'name': 84, 'parent': '11'}, {'color': '#FFF', 'name': 98, 'parent': '11'}]}, {'color': 'lightsteelblue', 'children_length': 5, 'name': '10', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 17, 'parent': '10'}, {'color': 'lightsteelblue', 'name': 49, 'parent': '10'}, {'color': 'lightsteelblue', 'name': 68, 'parent': '10'}, {'color': '#FFF', 'name': 76, 'parent': '10'}, {'color': '#FFF', 'name': 85, 'parent': '10'}]}, {'color': 'lightsteelblue', 'children_length': 11, 'name': '12', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 21, 'parent': '12'}, {'color': '#FFF', 'name': 23, 'parent': '12'}, {'color': '#FFF', 'name': 24, 'parent': '12'}, {'color': '#FFF', 'name': 25, 'parent': '12'}, {'color': '#FFF', 'name': 28, 'parent': '12'}, {'color': 'lightsteelblue', 'name': 34, 'parent': '12'}, {'color': 'lightsteelblue', 'name': 39, 'parent': '12'}, {'color': 'lightsteelblue', 'name': 64, 'parent': '12'}, {'color': 'lightsteelblue', 'name': 70, 'parent': '12'}, {'color': '#FFF', 'name': 77, 'parent': '12'}, {'color': '#FFF', 'name': 94, 'parent': '12'}]}, {'color': 'lightsteelblue', 'children_length': 2, 'name': '15', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 14, 'parent': '15'}, {'color': '#FFF', 'name': 50, 'parent': '15'}]}, {'color': 'lightsteelblue', 'children_length': 1, 'name': '14', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 18, 'parent': '14'}]}, {'color': 'lightsteelblue', 'children_length': 2, 'name': '17', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 22, 'parent': '17'}, {'color': 'lightsteelblue', 'name': 53, 'parent': '17'}]}, {'color': '#FFF', 'children_length': 4, 'name': '16', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 54, 'parent': '16'}, {'color': '#FFF', 'name': 62, 'parent': '16'}, {'color': '#FFF', 'name': 63, 'parent': '16'}, {'color': '#FFF', 'name': 71, 'parent': '16'}]}, {'color': 'lightsteelblue', 'children_length': 5, 'name': '19', 'parent': 'chromosome', '_children': [{'color': 'lightsteelblue', 'name': 37, 'parent': '19'}, {'color': 'lightsteelblue', 'name': 40, 'parent': '19'}, {'color': 'lightsteelblue', 'name': 41, 'parent': '19'}, {'color': 'lightsteelblue', 'name': 42, 'parent': '19'}, {'color': 'lightsteelblue', 'name': 47, 'parent': '19'}]}, {'color': '#FFF', 'children_length': 1, 'name': '18', 'parent': 'chromosome', '_children': [{'color': '#FFF', 'name': 97, 'parent': '18'}]}]}]

//arbre sur chromosome avec calque sur strand
//var treeData=[{'color': '#FFF', 'children_length': 22, 'name': 'chromosome', 'parent': 'null', '_children': [{'color': '#FFF', 'children_length': 4, 'name': '20', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 9, 'parent': '20'}, {'color': '#fc9272', 'name': 27, 'parent': '20'}, {'color': '#fee0d2', 'name': 81, 'parent': '20'}, {'color': '#fee0d2', 'name': 92, 'parent': '20'}]}, {'color': '#FFF', 'children_length': 1, 'name': '21', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 13, 'parent': '21'}]}, {'color': '#FFF', 'children_length': 5, 'name': '22', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 7, 'parent': '22'}, {'color': '#fee0d2', 'name': 20, 'parent': '22'}, {'color': '#fee0d2', 'name': 32, 'parent': '22'}, {'color': '#fc9272', 'name': 52, 'parent': '22'}, {'color': '#fee0d2', 'name': 66, 'parent': '22'}]}, {'color': '#FFF', 'children_length': 7, 'name': '1', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 26, 'parent': '1'}, {'color': '#fc9272', 'name': 30, 'parent': '1'}, {'color': '#fee0d2', 'name': 36, 'parent': '1'}, {'color': '#fc9272', 'name': 46, 'parent': '1'}, {'color': '#fc9272', 'name': 80, 'parent': '1'}, {'color': '#fc9272', 'name': 83, 'parent': '1'}, {'color': '#fc9272', 'name': 89, 'parent': '1'}]}, {'color': '#FFF', 'children_length': 5, 'name': '3', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 11, 'parent': '3'}, {'color': '#fee0d2', 'name': 16, 'parent': '3'}, {'color': '#fc9272', 'name': 44, 'parent': '3'}, {'color': '#fc9272', 'name': 67, 'parent': '3'}, {'color': '#fee0d2', 'name': 90, 'parent': '3'}]}, {'color': '#FFF', 'children_length': 8, 'name': '2', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 4, 'parent': '2'}, {'color': '#fee0d2', 'name': 5, 'parent': '2'}, {'color': '#fc9272', 'name': 6, 'parent': '2'}, {'color': '#fee0d2', 'name': 43, 'parent': '2'}, {'color': '#fc9272', 'name': 51, 'parent': '2'}, {'color': '#fc9272', 'name': 57, 'parent': '2'}, {'color': '#fee0d2', 'name': 87, 'parent': '2'}, {'color': '#fee0d2', 'name': 96, 'parent': '2'}]}, {'color': '#FFF', 'children_length': 6, 'name': '5', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 45, 'parent': '5'}, {'color': '#fc9272', 'name': 48, 'parent': '5'}, {'color': '#fc9272', 'name': 65, 'parent': '5'}, {'color': '#fee0d2', 'name': 74, 'parent': '5'}, {'color': '#fee0d2', 'name': 86, 'parent': '5'}, {'color': '#fee0d2', 'name': 95, 'parent': '5'}]}, {'color': '#FFF', 'children_length': 1, 'name': '4', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 3, 'parent': '4'}]}, {'color': '#FFF', 'children_length': 3, 'name': '7', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 29, 'parent': '7'}, {'color': '#fc9272', 'name': 75, 'parent': '7'}, {'color': '#fc9272', 'name': 93, 'parent': '7'}]}, {'color': '#FFF', 'children_length': 7, 'name': '6', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 1, 'parent': '6'}, {'color': '#fc9272', 'name': 8, 'parent': '6'}, {'color': '#fc9272', 'name': 12, 'parent': '6'}, {'color': '#fc9272', 'name': 33, 'parent': '6'}, {'color': '#fc9272', 'name': 38, 'parent': '6'}, {'color': '#fc9272', 'name': 59, 'parent': '6'}, {'color': '#fee0d2', 'name': 88, 'parent': '6'}]}, {'color': '#FFF', 'children_length': 3, 'name': '9', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 31, 'parent': '9'}, {'color': '#fee0d2', 'name': 69, 'parent': '9'}, {'color': '#fc9272', 'name': 72, 'parent': '9'}]}, {'color': '#FFF', 'children_length': 9, 'name': '8', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 2, 'parent': '8'}, {'color': '#fee0d2', 'name': 10, 'parent': '8'}, {'color': '#fee0d2', 'name': 15, 'parent': '8'}, {'color': '#fee0d2', 'name': 56, 'parent': '8'}, {'color': '#fee0d2', 'name': 58, 'parent': '8'}, {'color': '#fc9272', 'name': 73, 'parent': '8'}, {'color': '#fee0d2', 'name': 78, 'parent': '8'}, {'color': '#fc9272', 'name': 79, 'parent': '8'}, {'color': '#fc9272', 'name': 82, 'parent': '8'}]}, {'color': '#FFF', 'children_length': 5, 'name': 'X', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 19, 'parent': 'X'}, {'color': '#fc9272', 'name': 35, 'parent': 'X'}, {'color': '#fee0d2', 'name': 55, 'parent': 'X'}, {'color': '#fc9272', 'name': 60, 'parent': 'X'}, {'color': '#fc9272', 'name': 91, 'parent': 'X'}]}, {'color': '#FFF', 'children_length': 3, 'name': '11', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 61, 'parent': '11'}, {'color': '#fee0d2', 'name': 84, 'parent': '11'}, {'color': '#fc9272', 'name': 98, 'parent': '11'}]}, {'color': '#FFF', 'children_length': 5, 'name': '10', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 17, 'parent': '10'}, {'color': '#fee0d2', 'name': 49, 'parent': '10'}, {'color': '#fee0d2', 'name': 68, 'parent': '10'}, {'color': '#fc9272', 'name': 76, 'parent': '10'}, {'color': '#fc9272', 'name': 85, 'parent': '10'}]}, {'color': '#FFF', 'children_length': 11, 'name': '12', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 21, 'parent': '12'}, {'color': '#fc9272', 'name': 23, 'parent': '12'}, {'color': '#fc9272', 'name': 24, 'parent': '12'}, {'color': '#fc9272', 'name': 25, 'parent': '12'}, {'color': '#fc9272', 'name': 28, 'parent': '12'}, {'color': '#fee0d2', 'name': 34, 'parent': '12'}, {'color': '#fee0d2', 'name': 39, 'parent': '12'}, {'color': '#fee0d2', 'name': 64, 'parent': '12'}, {'color': '#fee0d2', 'name': 70, 'parent': '12'}, {'color': '#fc9272', 'name': 77, 'parent': '12'}, {'color': '#fc9272', 'name': 94, 'parent': '12'}]}, {'color': '#FFF', 'children_length': 2, 'name': '15', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 14, 'parent': '15'}, {'color': '#fc9272', 'name': 50, 'parent': '15'}]}, {'color': '#FFF', 'children_length': 1, 'name': '14', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 18, 'parent': '14'}]}, {'color': '#FFF', 'children_length': 2, 'name': '17', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 22, 'parent': '17'}, {'color': '#fee0d2', 'name': 53, 'parent': '17'}]}, {'color': '#FFF', 'children_length': 4, 'name': '16', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 54, 'parent': '16'}, {'color': '#fc9272', 'name': 62, 'parent': '16'}, {'color': '#fc9272', 'name': 63, 'parent': '16'}, {'color': '#fc9272', 'name': 71, 'parent': '16'}]}, {'color': '#FFF', 'children_length': 5, 'name': '19', 'parent': 'chromosome', '_children': [{'color': '#fee0d2', 'name': 37, 'parent': '19'}, {'color': '#fee0d2', 'name': 40, 'parent': '19'}, {'color': '#fee0d2', 'name': 41, 'parent': '19'}, {'color': '#fee0d2', 'name': 42, 'parent': '19'}, {'color': '#fee0d2', 'name': 47, 'parent': '19'}]}, {'color': '#FFF', 'children_length': 1, 'name': '18', 'parent': 'chromosome', '_children': [{'color': '#fc9272', 'name': 97, 'parent': '18'}]}]}]

//arbre sur strand avec calque sur chromosome
//var treeData=[{'color': '#FFF', 'children_length': 2, 'name': 'strand', 'parent': 'null', '_children': [{'color': '#FFF', 'children_length': 47, 'name': '+', 'parent': 'strand', '_children': [{'color': '#f0f0f0', 'name': 1, 'parent': '+'}, {'color': '#756bb1', 'name': 4, 'parent': '+'}, {'color': '#756bb1', 'name': 5, 'parent': '+'}, {'color': '#de2d26', 'name': 7, 'parent': '+'}, {'color': '#636363', 'name': 10, 'parent': '+'}, {'color': '#9ecae1', 'name': 14, 'parent': '+'}, {'color': '#636363', 'name': 15, 'parent': '+'}, {'color': '#bcbddc', 'name': 16, 'parent': '+'}, {'color': '#31a354', 'name': 17, 'parent': '+'}, {'color': '#3182bd', 'name': 18, 'parent': '+'}, {'color': '#e5f5e0', 'name': 19, 'parent': '+'}, {'color': '#de2d26', 'name': 20, 'parent': '+'}, {'color': '#fee0d2', 'name': 22, 'parent': '+'}, {'color': '#e6550d', 'name': 29, 'parent': '+'}, {'color': '#de2d26', 'name': 32, 'parent': '+'}, {'color': '#deebf7', 'name': 34, 'parent': '+'}, {'color': '#efedf5', 'name': 36, 'parent': '+'}, {'color': '#de2d26', 'name': 37, 'parent': '+'}, {'color': '#deebf7', 'name': 39, 'parent': '+'}, {'color': '#de2d26', 'name': 40, 'parent': '+'}, {'color': '#de2d26', 'name': 41, 'parent': '+'}, {'color': '#de2d26', 'name': 42, 'parent': '+'}, {'color': '#756bb1', 'name': 43, 'parent': '+'}, {'color': '#fee6ce', 'name': 45, 'parent': '+'}, {'color': '#de2d26', 'name': 47, 'parent': '+'}, {'color': '#31a354', 'name': 49, 'parent': '+'}, {'color': '#fee0d2', 'name': 53, 'parent': '+'}, {'color': '#e5f5e0', 'name': 55, 'parent': '+'}, {'color': '#636363', 'name': 56, 'parent': '+'}, {'color': '#636363', 'name': 58, 'parent': '+'}, {'color': '#a1d99b', 'name': 61, 'parent': '+'}, {'color': '#deebf7', 'name': 64, 'parent': '+'}, {'color': '#de2d26', 'name': 66, 'parent': '+'}, {'color': '#31a354', 'name': 68, 'parent': '+'}, {'color': '#bdbdbd', 'name': 69, 'parent': '+'}, {'color': '#deebf7', 'name': 70, 'parent': '+'}, {'color': '#fee6ce', 'name': 74, 'parent': '+'}, {'color': '#636363', 'name': 78, 'parent': '+'}, {'color': '#fee0d2', 'name': 81, 'parent': '+'}, {'color': '#a1d99b', 'name': 84, 'parent': '+'}, {'color': '#fee6ce', 'name': 86, 'parent': '+'}, {'color': '#756bb1', 'name': 87, 'parent': '+'}, {'color': '#f0f0f0', 'name': 88, 'parent': '+'}, {'color': '#bcbddc', 'name': 90, 'parent': '+'}, {'color': '#fee0d2', 'name': 92, 'parent': '+'}, {'color': '#fee6ce', 'name': 95, 'parent': '+'}, {'color': '#756bb1', 'name': 96, 'parent': '+'}]}, {'color': '#FFF', 'children_length': 51, 'name': '-', 'parent': 'strand', '_children': [{'color': '#636363', 'name': 2, 'parent': '-'}, {'color': '#fdae6b', 'name': 3, 'parent': '-'}, {'color': '#756bb1', 'name': 6, 'parent': '-'}, {'color': '#f0f0f0', 'name': 8, 'parent': '-'}, {'color': '#fee0d2', 'name': 9, 'parent': '-'}, {'color': '#bcbddc', 'name': 11, 'parent': '-'}, {'color': '#f0f0f0', 'name': 12, 'parent': '-'}, {'color': '#fc9272', 'name': 13, 'parent': '-'}, {'color': '#deebf7', 'name': 21, 'parent': '-'}, {'color': '#deebf7', 'name': 23, 'parent': '-'}, {'color': '#deebf7', 'name': 24, 'parent': '-'}, {'color': '#deebf7', 'name': 25, 'parent': '-'}, {'color': '#efedf5', 'name': 26, 'parent': '-'}, {'color': '#fee0d2', 'name': 27, 'parent': '-'}, {'color': '#deebf7', 'name': 28, 'parent': '-'}, {'color': '#efedf5', 'name': 30, 'parent': '-'}, {'color': '#bdbdbd', 'name': 31, 'parent': '-'}, {'color': '#f0f0f0', 'name': 33, 'parent': '-'}, {'color': '#e5f5e0', 'name': 35, 'parent': '-'}, {'color': '#f0f0f0', 'name': 38, 'parent': '-'}, {'color': '#bcbddc', 'name': 44, 'parent': '-'}, {'color': '#efedf5', 'name': 46, 'parent': '-'}, {'color': '#fee6ce', 'name': 48, 'parent': '-'}, {'color': '#9ecae1', 'name': 50, 'parent': '-'}, {'color': '#756bb1', 'name': 51, 'parent': '-'}, {'color': '#de2d26', 'name': 52, 'parent': '-'}, {'color': '#fc9272', 'name': 54, 'parent': '-'}, {'color': '#756bb1', 'name': 57, 'parent': '-'}, {'color': '#f0f0f0', 'name': 59, 'parent': '-'}, {'color': '#e5f5e0', 'name': 60, 'parent': '-'}, {'color': '#fc9272', 'name': 62, 'parent': '-'}, {'color': '#fc9272', 'name': 63, 'parent': '-'}, {'color': '#fee6ce', 'name': 65, 'parent': '-'}, {'color': '#bcbddc', 'name': 67, 'parent': '-'}, {'color': '#fc9272', 'name': 71, 'parent': '-'}, {'color': '#bdbdbd', 'name': 72, 'parent': '-'}, {'color': '#636363', 'name': 73, 'parent': '-'}, {'color': '#e6550d', 'name': 75, 'parent': '-'}, {'color': '#31a354', 'name': 76, 'parent': '-'}, {'color': '#deebf7', 'name': 77, 'parent': '-'}, {'color': '#636363', 'name': 79, 'parent': '-'}, {'color': '#efedf5', 'name': 80, 'parent': '-'}, {'color': '#636363', 'name': 82, 'parent': '-'}, {'color': '#efedf5', 'name': 83, 'parent': '-'}, {'color': '#31a354', 'name': 85, 'parent': '-'}, {'color': '#efedf5', 'name': 89, 'parent': '-'}, {'color': '#e5f5e0', 'name': 91, 'parent': '-'}, {'color': '#e6550d', 'name': 93, 'parent': '-'}, {'color': '#deebf7', 'name': 94, 'parent': '-'}, {'color': '#efedf5', 'name': 97, 'parent': '-'}, {'color': '#a1d99b', 'name': 98, 'parent': '-'}]}]}]


//arbre sur strand avec calque sur chromosome
//var treeData=[{'color': '#FFF', 'children_length': 2, 'name': 'strand', 'parent': 'null', '_children': [{'color': '#FFF', 'children_length': 47, 'name': '+', 'parent': 'strand', '_children': [{'color': '#f0f0f0', 'name': 1, 'parent': '+'}, {'color': '#636363', 'name': 4, 'parent': '+'}, {'color': '#bdbdbd', 'name': 5, 'parent': '+'}, {'color': '#fee0d2', 'name': 7, 'parent': '+'}, {'color': '#e5f5e0', 'name': 10, 'parent': '+'}, {'color': '#31a354', 'name': 14, 'parent': '+'}, {'color': '#f0f0f0', 'name': 15, 'parent': '+'}, {'color': '#bcbddc', 'name': 16, 'parent': '+'}, {'color': '#3182bd', 'name': 17, 'parent': '+'}, {'color': '#bcbddc', 'name': 18, 'parent': '+'}, {'color': '#e6550d', 'name': 19, 'parent': '+'}, {'color': '#deebf7', 'name': 20, 'parent': '+'}, {'color': '#e5f5e0', 'name': 22, 'parent': '+'}, {'color': '#e5f5e0', 'name': 29, 'parent': '+'}, {'color': '#e6550d', 'name': 32, 'parent': '+'}, {'color': '#de2d26', 'name': 34, 'parent': '+'}, {'color': '#a1d99b', 'name': 36, 'parent': '+'}, {'color': '#756bb1', 'name': 37, 'parent': '+'}, {'color': '#fee0d2', 'name': 39, 'parent': '+'}, {'color': '#fdae6b', 'name': 40, 'parent': '+'}, {'color': '#e6550d', 'name': 41, 'parent': '+'}, {'color': '#e5f5e0', 'name': 42, 'parent': '+'}, {'color': '#bdbdbd', 'name': 43, 'parent': '+'}, {'color': '#e5f5e0', 'name': 45, 'parent': '+'}, {'color': '#a1d99b', 'name': 47, 'parent': '+'}, {'color': '#3182bd', 'name': 49, 'parent': '+'}, {'color': '#fc9272', 'name': 53, 'parent': '+'}, {'color': '#fc9272', 'name': 55, 'parent': '+'}, {'color': '#756bb1', 'name': 56, 'parent': '+'}, {'color': '#9ecae1', 'name': 58, 'parent': '+'}, {'color': '#fee6ce', 'name': 61, 'parent': '+'}, {'color': '#de2d26', 'name': 64, 'parent': '+'}, {'color': '#deebf7', 'name': 66, 'parent': '+'}, {'color': '#756bb1', 'name': 68, 'parent': '+'}, {'color': '#a1d99b', 'name': 69, 'parent': '+'}, {'color': '#de2d26', 'name': 70, 'parent': '+'}, {'color': '#efedf5', 'name': 74, 'parent': '+'}, {'color': '#e6550d', 'name': 78, 'parent': '+'}, {'color': '#fc9272', 'name': 81, 'parent': '+'}, {'color': '#a1d99b', 'name': 84, 'parent': '+'}, {'color': '#bdbdbd', 'name': 86, 'parent': '+'}, {'color': '#fee0d2', 'name': 87, 'parent': '+'}, {'color': '#deebf7', 'name': 88, 'parent': '+'}, {'color': '#de2d26', 'name': 90, 'parent': '+'}, {'color': '#bcbddc', 'name': 92, 'parent': '+'}, {'color': '#e6550d', 'name': 95, 'parent': '+'}, {'color': '#de2d26', 'name': 96, 'parent': '+'}]}, {'color': '#FFF', 'children_length': 51, 'name': '-', 'parent': 'strand', '_children': [{'color': '#756bb1', 'name': 2, 'parent': '-'}, {'color': '#f0f0f0', 'name': 3, 'parent': '-'}, {'color': '#31a354', 'name': 6, 'parent': '-'}, {'color': '#fc9272', 'name': 8, 'parent': '-'}, {'color': '#bdbdbd', 'name': 9, 'parent': '-'}, {'color': '#fee0d2', 'name': 11, 'parent': '-'}, {'color': '#636363', 'name': 12, 'parent': '-'}, {'color': '#fee0d2', 'name': 13, 'parent': '-'}, {'color': '#fc9272', 'name': 21, 'parent': '-'}, {'color': '#fee0d2', 'name': 23, 'parent': '-'}, {'color': '#bdbdbd', 'name': 24, 'parent': '-'}, {'color': '#e6550d', 'name': 25, 'parent': '-'}, {'color': '#3182bd', 'name': 26, 'parent': '-'}, {'color': '#e6550d', 'name': 27, 'parent': '-'}, {'color': '#bdbdbd', 'name': 28, 'parent': '-'}, {'color': '#e5f5e0', 'name': 30, 'parent': '-'}, {'color': '#e5f5e0', 'name': 31, 'parent': '-'}, {'color': '#fdae6b', 'name': 33, 'parent': '-'}, {'color': '#fee0d2', 'name': 35, 'parent': '-'}, {'color': '#a1d99b', 'name': 38, 'parent': '-'}, {'color': '#de2d26', 'name': 44, 'parent': '-'}, {'color': '#deebf7', 'name': 46, 'parent': '-'}, {'color': '#fc9272', 'name': 48, 'parent': '-'}, {'color': '#756bb1', 'name': 50, 'parent': '-'}, {'color': '#e6550d', 'name': 51, 'parent': '-'}, {'color': '#fee0d2', 'name': 52, 'parent': '-'}, {'color': '#e5f5e0', 'name': 54, 'parent': '-'}, {'color': '#bdbdbd', 'name': 57, 'parent': '-'}, {'color': '#f0f0f0', 'name': 59, 'parent': '-'}, {'color': '#756bb1', 'name': 60, 'parent': '-'}, {'color': '#deebf7', 'name': 62, 'parent': '-'}, {'color': '#bcbddc', 'name': 63, 'parent': '-'}, {'color': '#fee6ce', 'name': 65, 'parent': '-'}, {'color': '#636363', 'name': 67, 'parent': '-'}, {'color': '#deebf7', 'name': 71, 'parent': '-'}, {'color': '#fc9272', 'name': 72, 'parent': '-'}, {'color': '#deebf7', 'name': 73, 'parent': '-'}, {'color': '#deebf7', 'name': 75, 'parent': '-'}, {'color': '#fdae6b', 'name': 76, 'parent': '-'}, {'color': '#9ecae1', 'name': 77, 'parent': '-'}, {'color': '#a1d99b', 'name': 79, 'parent': '-'}, {'color': '#3182bd', 'name': 80, 'parent': '-'}, {'color': '#fee6ce', 'name': 82, 'parent': '-'}, {'color': '#756bb1', 'name': 83, 'parent': '-'}, {'color': '#fdae6b', 'name': 85, 'parent': '-'}, {'color': '#fc9272', 'name': 89, 'parent': '-'}, {'color': '#efedf5', 'name': 91, 'parent': '-'}, {'color': '#bcbddc', 'name': 93, 'parent': '-'}, {'color': '#9ecae1', 'name': 94, 'parent': '-'}, {'color': '#756bb1', 'name': 97, 'parent': '-'}, {'color': '#fee6ce', 'name': 98, 'parent': '-'}]}]}]

var treeData=[{'layer': 'chromosome', 'name': 'strand', 'parent': 'null', 'children': [{'layer': 'null', 'name': '+', 'parent': 'strand', '_children': [{'layer': 'chromosome', 'name': '1-10', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 1, 'parent': '1-10', '_children': [], 'color': '#31a354', 'children_length': 0}, {'layer': 'chromosome', 'name': 4, 'parent': '1-10', '_children': [], 'color': '#f0f0f0', 'children_length': 0}, {'layer': 'chromosome', 'name': 5, 'parent': '1-10', '_children': [], 'color': '#f0f0f0', 'children_length': 0}, {'layer': 'chromosome', 'name': 7, 'parent': '1-10', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 10, 'parent': '1-10', '_children': [], 'color': '#e5f5e0', 'children_length': 0}], 'color': '#FFF', 'children_length': 5}, {'layer': 'chromosome', 'name': '14-19', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 14, 'parent': '14-19', '_children': [], 'color': '#fdae6b', 'children_length': 0}, {'layer': 'chromosome', 'name': 15, 'parent': '14-19', '_children': [], 'color': '#e5f5e0', 'children_length': 0}, {'layer': 'chromosome', 'name': 16, 'parent': '14-19', '_children': [], 'color': '#9ecae1', 'children_length': 0}, {'layer': 'chromosome', 'name': 17, 'parent': '14-19', '_children': [], 'color': '#de2d26', 'children_length': 0}, {'layer': 'chromosome', 'name': 18, 'parent': '14-19', '_children': [], 'color': '#fee0d2', 'children_length': 0}, {'layer': 'chromosome', 'name': 19, 'parent': '14-19', '_children': [], 'color': '#bdbdbd', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '20-36', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 20, 'parent': '20-36', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 22, 'parent': '20-36', '_children': [], 'color': '#fc9272', 'children_length': 0}, {'layer': 'chromosome', 'name': 29, 'parent': '20-36', '_children': [], 'color': '#deebf7', 'children_length': 0}, {'layer': 'chromosome', 'name': 32, 'parent': '20-36', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 34, 'parent': '20-36', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 36, 'parent': '20-36', '_children': [], 'color': '#a1d99b', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '37-43', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 37, 'parent': '37-43', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 39, 'parent': '37-43', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 40, 'parent': '37-43', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 41, 'parent': '37-43', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 42, 'parent': '37-43', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 43, 'parent': '37-43', '_children': [], 'color': '#f0f0f0', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '45-56', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 45, 'parent': '45-56', '_children': [], 'color': '#efedf5', 'children_length': 0}, {'layer': 'chromosome', 'name': 47, 'parent': '45-56', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 49, 'parent': '45-56', '_children': [], 'color': '#de2d26', 'children_length': 0}, {'layer': 'chromosome', 'name': 53, 'parent': '45-56', '_children': [], 'color': '#fc9272', 'children_length': 0}, {'layer': 'chromosome', 'name': 55, 'parent': '45-56', '_children': [], 'color': '#bdbdbd', 'children_length': 0}, {'layer': 'chromosome', 'name': 56, 'parent': '45-56', '_children': [], 'color': '#e5f5e0', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '58-69', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 58, 'parent': '58-69', '_children': [], 'color': '#e5f5e0', 'children_length': 0}, {'layer': 'chromosome', 'name': 61, 'parent': '58-69', '_children': [], 'color': '#636363', 'children_length': 0}, {'layer': 'chromosome', 'name': 64, 'parent': '58-69', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 66, 'parent': '58-69', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 68, 'parent': '58-69', '_children': [], 'color': '#de2d26', 'children_length': 0}, {'layer': 'chromosome', 'name': 69, 'parent': '58-69', '_children': [], 'color': '#bcbddc', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '70-86', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 70, 'parent': '70-86', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 74, 'parent': '70-86', '_children': [], 'color': '#efedf5', 'children_length': 0}, {'layer': 'chromosome', 'name': 78, 'parent': '70-86', '_children': [], 'color': '#e5f5e0', 'children_length': 0}, {'layer': 'chromosome', 'name': 81, 'parent': '70-86', '_children': [], 'color': '#fc9272', 'children_length': 0}, {'layer': 'chromosome', 'name': 84, 'parent': '70-86', '_children': [], 'color': '#636363', 'children_length': 0}, {'layer': 'chromosome', 'name': 86, 'parent': '70-86', '_children': [], 'color': '#efedf5', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '87-96', 'parent': '+', '_children': [{'layer': 'chromosome', 'name': 87, 'parent': '87-96', '_children': [], 'color': '#f0f0f0', 'children_length': 0}, {'layer': 'chromosome', 'name': 88, 'parent': '87-96', '_children': [], 'color': '#31a354', 'children_length': 0}, {'layer': 'chromosome', 'name': 90, 'parent': '87-96', '_children': [], 'color': '#9ecae1', 'children_length': 0}, {'layer': 'chromosome', 'name': 92, 'parent': '87-96', '_children': [], 'color': '#fc9272', 'children_length': 0}, {'layer': 'chromosome', 'name': 95, 'parent': '87-96', '_children': [], 'color': '#efedf5', 'children_length': 0}, {'layer': 'chromosome', 'name': 96, 'parent': '87-96', '_children': [], 'color': '#f0f0f0', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}], 'color': '#FFF', 'children_length': 8}, {'layer': 'null', 'name': '-', 'parent': 'strand', '_children': [{'layer': 'chromosome', 'name': '2-11', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 2, 'parent': '2-11', '_children': [], 'color': '#e5f5e0', 'children_length': 0}, {'layer': 'chromosome', 'name': 3, 'parent': '2-11', '_children': [], 'color': '#756bb1', 'children_length': 0}, {'layer': 'chromosome', 'name': 6, 'parent': '2-11', '_children': [], 'color': '#f0f0f0', 'children_length': 0}, {'layer': 'chromosome', 'name': 8, 'parent': '2-11', '_children': [], 'color': '#31a354', 'children_length': 0}, {'layer': 'chromosome', 'name': 9, 'parent': '2-11', '_children': [], 'color': '#fc9272', 'children_length': 0}, {'layer': 'chromosome', 'name': 11, 'parent': '2-11', '_children': [], 'color': '#9ecae1', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '12-25', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 12, 'parent': '12-25', '_children': [], 'color': '#31a354', 'children_length': 0}, {'layer': 'chromosome', 'name': 13, 'parent': '12-25', '_children': [], 'color': '#3182bd', 'children_length': 0}, {'layer': 'chromosome', 'name': 21, 'parent': '12-25', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 23, 'parent': '12-25', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 24, 'parent': '12-25', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 25, 'parent': '12-25', '_children': [], 'color': '#fee6ce', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '26-33', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 26, 'parent': '26-33', '_children': [], 'color': '#a1d99b', 'children_length': 0}, {'layer': 'chromosome', 'name': 27, 'parent': '26-33', '_children': [], 'color': '#fc9272', 'children_length': 0}, {'layer': 'chromosome', 'name': 28, 'parent': '26-33', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 30, 'parent': '26-33', '_children': [], 'color': '#a1d99b', 'children_length': 0}, {'layer': 'chromosome', 'name': 31, 'parent': '26-33', '_children': [], 'color': '#bcbddc', 'children_length': 0}, {'layer': 'chromosome', 'name': 33, 'parent': '26-33', '_children': [], 'color': '#31a354', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '35-51', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 35, 'parent': '35-51', '_children': [], 'color': '#bdbdbd', 'children_length': 0}, {'layer': 'chromosome', 'name': 38, 'parent': '35-51', '_children': [], 'color': '#31a354', 'children_length': 0}, {'layer': 'chromosome', 'name': 44, 'parent': '35-51', '_children': [], 'color': '#9ecae1', 'children_length': 0}, {'layer': 'chromosome', 'name': 46, 'parent': '35-51', '_children': [], 'color': '#a1d99b', 'children_length': 0}, {'layer': 'chromosome', 'name': 48, 'parent': '35-51', '_children': [], 'color': '#efedf5', 'children_length': 0}, {'layer': 'chromosome', 'name': 50, 'parent': '35-51', '_children': [], 'color': '#fdae6b', 'children_length': 0}, {'layer': 'chromosome', 'name': 51, 'parent': '35-51', '_children': [], 'color': '#f0f0f0', 'children_length': 0}], 'color': '#FFF', 'children_length': 7}, {'layer': 'chromosome', 'name': '52-62', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 52, 'parent': '52-62', '_children': [], 'color': '#e6550d', 'children_length': 0}, {'layer': 'chromosome', 'name': 54, 'parent': '52-62', '_children': [], 'color': '#3182bd', 'children_length': 0}, {'layer': 'chromosome', 'name': 57, 'parent': '52-62', '_children': [], 'color': '#f0f0f0', 'children_length': 0}, {'layer': 'chromosome', 'name': 59, 'parent': '52-62', '_children': [], 'color': '#31a354', 'children_length': 0}, {'layer': 'chromosome', 'name': 60, 'parent': '52-62', '_children': [], 'color': '#bdbdbd', 'children_length': 0}, {'layer': 'chromosome', 'name': 62, 'parent': '52-62', '_children': [], 'color': '#3182bd', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '63-75', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 63, 'parent': '63-75', '_children': [], 'color': '#3182bd', 'children_length': 0}, {'layer': 'chromosome', 'name': 65, 'parent': '63-75', '_children': [], 'color': '#efedf5', 'children_length': 0}, {'layer': 'chromosome', 'name': 67, 'parent': '63-75', '_children': [], 'color': '#9ecae1', 'children_length': 0}, {'layer': 'chromosome', 'name': 71, 'parent': '63-75', '_children': [], 'color': '#3182bd', 'children_length': 0}, {'layer': 'chromosome', 'name': 72, 'parent': '63-75', '_children': [], 'color': '#bcbddc', 'children_length': 0}, {'layer': 'chromosome', 'name': 73, 'parent': '63-75', '_children': [], 'color': '#e5f5e0', 'children_length': 0}, {'layer': 'chromosome', 'name': 75, 'parent': '63-75', '_children': [], 'color': '#deebf7', 'children_length': 0}], 'color': '#FFF', 'children_length': 7}, {'layer': 'chromosome', 'name': '76-83', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 76, 'parent': '76-83', '_children': [], 'color': '#de2d26', 'children_length': 0}, {'layer': 'chromosome', 'name': 77, 'parent': '76-83', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 79, 'parent': '76-83', '_children': [], 'color': '#e5f5e0', 'children_length': 0}, {'layer': 'chromosome', 'name': 80, 'parent': '76-83', '_children': [], 'color': '#a1d99b', 'children_length': 0}, {'layer': 'chromosome', 'name': 82, 'parent': '76-83', '_children': [], 'color': '#e5f5e0', 'children_length': 0}, {'layer': 'chromosome', 'name': 83, 'parent': '76-83', '_children': [], 'color': '#a1d99b', 'children_length': 0}], 'color': '#FFF', 'children_length': 6}, {'layer': 'chromosome', 'name': '85-98', 'parent': '-', '_children': [{'layer': 'chromosome', 'name': 85, 'parent': '85-98', '_children': [], 'color': '#de2d26', 'children_length': 0}, {'layer': 'chromosome', 'name': 89, 'parent': '85-98', '_children': [], 'color': '#a1d99b', 'children_length': 0}, {'layer': 'chromosome', 'name': 91, 'parent': '85-98', '_children': [], 'color': '#bdbdbd', 'children_length': 0}, {'layer': 'chromosome', 'name': 93, 'parent': '85-98', '_children': [], 'color': '#deebf7', 'children_length': 0}, {'layer': 'chromosome', 'name': 94, 'parent': '85-98', '_children': [], 'color': '#fee6ce', 'children_length': 0}, {'layer': 'chromosome', 'name': 97, 'parent': '85-98', '_children': [], 'color': '#a1d99b', 'children_length': 0}, {'layer': 'chromosome', 'name': 98, 'parent': '85-98', '_children': [], 'color': '#636363', 'children_length': 0}], 'color': '#FFF', 'children_length': 7}], 'color': '#FFF', 'children_length': 8}], 'color': '#FFF', 'children_length': 2}]

//************************************************************functions************************************************





//************************************************************functions************************************************
function update(source) {


  // Compute the new tree layout.
  var nodes = tree.nodes(root).reverse(),
	  links = tree.links(nodes);

  // Normalize for fixed-depth.
  nodes.forEach(function(d) {d.y = d.depth * 100;});

  // Update the nodes…
  var node = svg.selectAll("g.node")
	  .data(nodes, function(d) { return d.id || (d.id = ++i); });


  // Enter any new nodes at the parent's previous position.
  var nodeEnter = node.enter().append("g")
	  //.attr("class", "node")
	  .attr("class", 'node')


  nodeEnter.append("circle")
	  .attr("r", 1e-6)
	  .style("fill", function(d) {return d.children ? "lightsteelblue" : "#fff"; });

  nodeEnter.append("text")
	  .attr("y",  function(d) {return d.children || d.children ?  -15: 25;})
	  .attr("x", function(d) { return d.children || d.children ? 10 : 0;})
	  .attr("text-anchor", 'middle')
	  .style("font-size",15)
	  .text(function(d) {if (d.parent == 'null'){return 'Tree : '+d.name+' / '+'Layer : '+d.layer; } else{return d.name;}})
	  .style("fill", function(d) {return d.children ? "black":"blue"; })
	  .style("fill-opacity", 1);

  nodeEnter.append("text")
	  .attr("y", 25)
	  .attr("x", 0)
	  .attr("text-anchor", 'middle')
	  .text(function(d) {if (d.children_length ){return d.children_length}})
	  .style("font-weight", 'bold')
	  .style("fill", 'black')
	  .style("fill-opacity", 1);



//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////



  // Transition nodes to their new position.
  var nodeUpdate = node.transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });



  nodeUpdate.select("circle")
	  .attr("r" , 10)                   // modifie le rayon des noeuds lorsque les noeud ss jacents sont absorbés
	  //.style("fill" , function(d) { return d.color} )           // change la couleur des noeuds


  nodeUpdate.select("text")
	  .style("fill-opacity", 1);



  nodeUpdate.select("text")
	  .style("fill-opacity", 1);

  d3.selectAll("g.node").select("circle")
      .style('fill','red');


  nodeUpdate.transition(pieChart(d3.selectAll("g.node"),data))
	  .duration(duration)




  //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

  // Transition exiting nodes to the parent's new position.
  var nodeExit = node.exit().transition()
	  .duration(duration)
	  .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; })
	  .remove();

  nodeExit.select("circle")
	  .attr("r", 1e-6);

  nodeExit.select("text")
      .style("fill-opacity", 1e-6);

  nodeExit.select("text.s")
      .style("fill-opacity", 1e-6);

  // Update the links…
  var link = svg.selectAll("path.link")
	  .data(links, function(d) { return d.target.id; });

  // Enter any new links at the parent's previous position.
  link.enter().insert("path", "g")
	  .attr("class", "link")
	  .attr("d", function(d) {
		var o = {x: source.x, y: source.y};
		return diagonal({source: o, target: o});
	  });


  // Transition links to their new position.
  link.transition()
	  .duration(duration)
	  .attr("d", diagonal);


  // Transition exiting nodes to the parent's new position.
  link.exit().transition()
      .duration(duration)
	  .attr("d", function(d) {
		var o = {x: source.x, y: source.y};
		return diagonal({source: o, target: o});
	    })
	  .remove();


	  // Stash the old positions for transition.
  nodes.forEach(function(d) {
	d.x0 = d.x;
	d.y0 = d.y;
  });

}

// Toggle children on click.
function click(d) {
  if (d.children) {
	d.children = d.children;
	d.children = null;
  } else {
	d.children = d.children;
	d.children = null;
  }
  update(d);
}

// ************** Generate the tree diagram	 *****************
var margin = {top: 30, right: 10, bottom: 30, left: 10},
	width = 1500 - margin.right - margin.left,
	height = 1500 - margin.top - margin.bottom;

var i = 0,
	duration = 300,
	root;

var tree = d3.layout.tree()
	.size([height, width]);

var diagonal = d3.svg.diagonal()
 .projection(function(d) { return [d.x, d.y]; });

var svg = d3.select("#visRow").append("svg")
	.attr("width", width + margin.right + margin.left)
	.attr("height", height + margin.top + margin.bottom)
    .append("g")
	.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

root = treeData[0];
root.x0 = height / 2;
root.y0 = 0;

update(root);



