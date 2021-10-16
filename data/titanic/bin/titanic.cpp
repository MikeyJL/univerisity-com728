/**
 * @file titanic.cpp
 * @author Mikey Lau (https://mikeylau.uk)
 * @brief A helper to load, transform, and explore the titanic dataset from https://kaggle.com
 * @version 1.0
 * @date 2021-10-16
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<string> row;
typedef vector<row> dataset;

struct AgeGroup
{
    int children;
    int adults;
    int elders;
};

struct FemaleMale
{
    int female;
    int male;
};

/**
 * Loads the titanic.csv data and prompts the user for an input between 1 and 5.
 * Options:
 * - 1: Get all names.
 * - 2: Get number of survivors.
 * - 3: Get male and females.
 * - 4: Get age groups.
 * - 5: Get age groups that survived.
 */
class TitanicData
{
    public:
        dataset data;
        TitanicData()
        {
            ifstream file;
            string line;
            file.open("../titanic.csv");
            if (!file.is_open())
                throw runtime_error("Could not open file");
            getline(file, line);
            while (getline(file, line))
            {
                row lineResult;
                stringstream ss(line);
                string str;
                while (getline(ss, str, ','))
                {
                    lineResult.push_back(str);
                }
                data.push_back(lineResult);
            }
            file.close();
        }

        /**
         * @return vector<string> - all the names in the dataset. 
         */
        vector<string> getNames()
        {
            vector<string> names;
            for (row passenger : data)
                names.push_back(passenger[3] + passenger[4]);
            return names;
        }

        /**
         * @return string - the number of survivors.
         */
        string passengerSurvived()
        {
            int survived = 0;
            for (row passenger : data)
                survived += passenger[1] == "1" ? 1 : 0;
            return to_string(survived);
        }

        /**
         * @return FemaleMale - the number of names and females.
         */
        FemaleMale femalesAndMales()
        {
            FemaleMale female_male;
            int males = 0;
            for (row passenger : data)
                males += passenger[5] == "male" ? 1 : 0;
            int females = (int)data.size() - males;
            female_male.female = females;
            female_male.male = males;
            return female_male;
        }

        /**
         * @return AgeGroup - age groups of children (<18), adults (18-64), and elders (>65).
         */
        AgeGroup passengerAgeGroups()
        {
            dataset cleanData;
            AgeGroup ageGroup;
            int children = 0;
            int adults = 0;
            int elders = 0;
            copy_if(data.begin(), data.end(), back_inserter(cleanData), [](row rawRow)
                    { return rawRow[6] != ""; });
            for (row passenger : cleanData)
                children += stof(passenger[6]) < 18 ? 1 : 0;
            for (row passenger : cleanData)
                adults += stof(passenger[6]) >= 18 && stof(passenger[6]) < 65 ? 1 : 0;
            for (row passenger : cleanData)
                elders += stof(passenger[6]) >= 65 ? 1 : 0;
            ageGroup.children = children;
            ageGroup.adults = adults;
            ageGroup.elders = elders;
            return ageGroup;
        }

        /**
         * @return AgeGroup - age groups of children (<18), adults (18-64), and elders (>65) that survived.
         */
        AgeGroup passengerAgeGroupsSurvived()
        {
            dataset cleanData;
            AgeGroup ageGroup;
            int sChildren = 0;
            int sAdults = 0;
            int sElders = 0;
            copy_if(data.begin(), data.end(), back_inserter(cleanData), [](row rawRow)
                    { return rawRow[6] != ""; });
            for (row passenger : cleanData)
                sChildren += stoi(passenger[6]) < 18 && passenger[1] == "1" ? 1 : 0;
            for (row passenger : cleanData)
                sAdults += stoi(passenger[6]) >= 18 && stoi(passenger[6]) < 65 && passenger[1] == "1" ? 1 : 0;
            for (row passenger : cleanData)
                sElders += stoi(passenger[6]) >= 65 && passenger[1] == "1" ? 1 : 0;
            ageGroup.children = sChildren;
            ageGroup.adults = sAdults;
            ageGroup.elders = sElders;
            return ageGroup;
        }
};

/**
 * Removes all occurrences of a character from a string.
 * @param S - the string to remove the characters from.
 * @param c - the character to remove.
 * @return string - the processed string. 
 */
string removeCharacters(string S, char c)
{
    S.erase(remove(
                S.begin(), S.end(), c),
            S.end());

    return S;
}

int main()
{
    string option;
    cout << "\nPlease select one of the following options:\n\n[1] Display the names of all passengers\n[2] Display the number of passengers that survived\n[3] Display the number of passengers per gender\n[4] Display the number of passengers per age group\n[5] Display the number of survivors per age group\n\nSelect an option\n>>> ";
    cin >> option;
    cout << "You've selected option: " << option << endl;

    TitanicData obj;
    if (option == "1")
    {
        vector<string> names = obj.getNames();
        for (string name : names)
            cout << removeCharacters(name, '"') << endl;
    }
    else if (option == "2")
        cout << "Survived: " << obj.passengerSurvived() << endl;
    else if (option == "3")
    {
        FemaleMale female_male = obj.femalesAndMales();
        cout << "females: " << female_male.female << " males: " << female_male.male << endl;
    }
    else if (option == "4")
    {
        AgeGroup ages = obj.passengerAgeGroups();
        cout << "children: " << ages.children << " adults:" << ages.adults << " elderly: " << ages.elders << endl;
    }
    else if (option == "5")
    {
        AgeGroup ages = obj.passengerAgeGroups();
        AgeGroup sAges = obj.passengerAgeGroupsSurvived();
        cout << "children: " << to_string(sAges.children) + "/" + to_string(ages.children) << " adults: " << to_string(sAges.adults) + "/" + to_string(ages.adults) << " elderly: " << to_string(sAges.elders) + "/" + to_string(ages.elders) << endl;
    }
    return 0;
}